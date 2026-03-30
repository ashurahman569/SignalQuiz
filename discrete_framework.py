import numpy as np
from scipy import signal  
  
class DiscreteSignal:  
    """  
    Represents a discrete-time signal.  
    """  
    def __init__(self, data):  
        # Ensure data is a numpy array, potentially complex  
        self.data = np.array(data, dtype=np.complex128)  
  
    def __len__(self):  
        return len(self.data)  
          
    def pad(self, new_length):  
        """  
        Zero-pad or truncate signal to new_length.  
        Returns a new DiscreteSignal object.  
        """  
        if len(self.data) > new_length:  
            # Truncate signal  
            return DiscreteSignal(self.data[:new_length])  
        else:  
            # Zero-pad signal  
            padded_data = np.zeros(new_length, dtype=np.complex128)  
            padded_data[:len(self.data)] = self.data  
            return DiscreteSignal(padded_data)  
  
    def interpolate(self, new_length):  
        """  
        Resample signal to new_length using linear interpolation.  
        Required for Task 1 (Drawing App) when using FFT.  
        """  
        if len(self.data) == 0:  
            return DiscreteSignal(np.zeros(new_length, dtype=np.complex128))  
        if len(self.data) == new_length:  
            return DiscreteSignal(self.data.copy())  
        if len(self.data) == 1:  
            return DiscreteSignal(np.full(new_length, self.data[0], dtype=np.complex128))  
          
        # Linear interpolation for complex signals  
        old_indices = np.arange(len(self.data))  
        new_indices = np.linspace(0, len(self.data) - 1, new_length)  
          
        # Interpolate real and imaginary parts separately  
        interpolated_real = np.interp(new_indices, old_indices, self.data.real)  
        interpolated_imag = np.interp(new_indices, old_indices, self.data.imag)  
        interpolated_data = interpolated_real + 1j * interpolated_imag  
          
        return DiscreteSignal(interpolated_data)  
  
  
class DFTAnalyzer:  
    """  
    Performs Discrete Fourier Transform using O(N^2) method.  
    """  
    def compute_dft(self, signal: DiscreteSignal):  
        """  
        Compute DFT using naive summation.  
        X[k] = sum_{n=0}^{N-1} x[n] * exp(-j*2*pi*k*n/N)  
        Returns: numpy array of complex frequency coefficients.  
        """  
        N = len(signal)  
        if N == 0:  
            return np.array([], dtype=np.complex128)  
          
        X = np.zeros(N, dtype=np.complex128)  
        for k in range(N):  
            for n in range(N):  
                X[k] += signal.data[n] * np.exp(-1j * 2 * np.pi * k * n / N)  
        return X  
  
    def compute_idft(self, spectrum):  
        """  
        Compute Inverse DFT using naive summation.  
        x[n] = (1/N) * sum_{k=0}^{N-1} X[k] * exp(j*2*pi*k*n/N)  
        Returns: numpy array (time-domain samples).  
        """  
        N = len(spectrum)  
        if N == 0:  
            return np.array([], dtype=np.complex128)  
          
        x = np.zeros(N, dtype=np.complex128)  
        for n in range(N):  
            for k in range(N):  
                x[n] += spectrum[k] * np.exp(1j * 2 * np.pi * k * n / N)  
            x[n] /= N  
        return x  
  
  
class FastFourierTransform(DFTAnalyzer):  
    """  
    Performs Fast Fourier Transform using Radix-2 Decimation-in-Time Cooley-Tukey Algorithm.  
    Complexity: O(N log N)  
    """  
      
    def next_power_of_2(self, n):  
        if n <= 0:  
            return 1  
        power = 1  
        while power < n:  
            power *= 2  
        return power  
      
    def fft_recursive(self, x):  
        """  
        Recursive Radix-2 DIT FFT implementation.  
        Input x must have length that is a power of 2.  
        """  
        N = len(x)  
          
        # Base case  
        if N == 1:  
            return x.copy()  
          
        x_even = x[0::2]  
        x_odd = x[1::2]  
          
        X_even = self.fft_recursive(x_even)  
        X_odd = self.fft_recursive(x_odd)  
          
        X = np.zeros(N, dtype=np.complex128)  
        for k in range(N // 2):  
            # Twiddle factor  
            W = np.exp(-1j * 2 * np.pi * k / N)  
            X[k] = X_even[k] + W * X_odd[k]  
            X[k + N // 2] = X_even[k] - W * X_odd[k]  
          
        return X  
      
    def ifft_recursive(self, X):  
        """  
        Recursive Radix-2 DIT IFFT implementation.  
        Input X must have length that is a power of 2.  
        """  
        N = len(X)  
          
        if N == 1:  
            return X.copy()  
          
        X_even = X[0::2]  
        X_odd = X[1::2]  
          
        x_even = self.ifft_recursive(X_even)  
        x_odd = self.ifft_recursive(X_odd)  
           
        x = np.zeros(N, dtype=np.complex128)  
        for k in range(N // 2):  
            # Twiddle factor for IFFT is conjugate of FFT twiddle factor 
            W = np.exp(1j * 2 * np.pi * k / N)  
            x[k] = x_even[k] + W * x_odd[k]  
            x[k + N // 2] = x_even[k] - W * x_odd[k]  
          
        return x  
      
    def compute_fft(self, signal: DiscreteSignal):  
        """  
        Compute FFT using Radix-2 Cooley-Tukey algorithm.  
        Automatically pads input to next power of 2 if necessary.  
        Returns: numpy array of complex frequency coefficients.  
        """  
        N = len(signal)  
        if N == 0:  
            return np.array([], dtype=np.complex128)  
          
        # Pad to next power of 2 if necessary  
        N_padded = self.next_power_of_2(N)  
        if N_padded != N:  
            padded_signal = signal.pad(N_padded)  
            data = padded_signal.data  
        else:  
            data = signal.data.copy()  
          
        return self.fft_recursive(data)  
      
    def compute_ifft(self, spectrum):  
        """  
        Compute IFFT using Radix-2 Cooley-Tukey algorithm.  
        Automatically pads input to next power of 2 if necessary.  
        Returns: numpy array (time-domain samples).  
        """  
        N = len(spectrum)  
        if N == 0:  
            return np.array([], dtype=np.complex128)  
          
        # Pad to next power of 2 if necessary  
        N_padded = self.next_power_of_2(N)  
        if N_padded != N:  
            padded_spectrum = np.zeros(N_padded, dtype=np.complex128)  
            padded_spectrum[:N] = spectrum  
            spectrum = padded_spectrum  
        else:  
            spectrum = np.array(spectrum, dtype=np.complex128)  
          
        # Computing IFFT and doing 1/N normalization  
        x = self.ifft_recursive(spectrum)  
        return x / len(spectrum)  
    
    def fft_recursive_dif(self, x):
        """
        Recursive Radix-2 DIF FFT implementation.
        Input x must have length that is a power of 2.
        """
        N = len(x)

        # Base case
        if N == 1:
            return x.copy()

        half = N // 2

        # Split the INPUT into first half and second half (frequency domain split)
        x_top = x[:half]
        x_bot = x[half:]

        # Apply twiddle factor BEFORE recursing (opposite of DIT)
        x_sum  = x_top + x_bot                                          # even output group
        x_diff = (x_top - x_bot) * np.exp(-1j * 2 * np.pi * np.arange(half) / N)  # odd output group

        # Recurse on combined halves
        X_even = self.fft_recursive_dif(x_sum)
        X_odd  = self.fft_recursive_dif(x_diff)

        # Interleave: even-indexed bins come from X_even, odd-indexed from X_odd
        X = np.zeros(N, dtype=np.complex128)
        X[0::2] = X_even
        X[1::2] = X_odd

        return X


    def ifft_recursive_dif(self, X):
        """
        Recursive Radix-2 DIF IFFT implementation.
        Twiddle factor uses conjugate: exp(+j*2*pi*k/N).
        Input X must have length that is a power of 2.
        """
        N = len(X)

        if N == 1:
            return X.copy()

        half = N // 2

        X_top = X[:half]
        X_bot = X[half:]

        X_sum  = X_top + X_bot
        X_diff = (X_top - X_bot) * np.exp(1j * 2 * np.pi * np.arange(half) / N)  # conjugate twiddle

        x_even = self.ifft_recursive_dif(X_sum)
        x_odd  = self.ifft_recursive_dif(X_diff)

        x = np.zeros(N, dtype=np.complex128)
        x[0::2] = x_even
        x[1::2] = x_odd

        return x

    def compute_fft_dif(self, signal: DiscreteSignal):
        """
        Compute FFT using Radix-2 DIF Cooley-Tukey algorithm.
        Automatically pads input to next power of 2 if necessary.
        Returns: numpy array of complex frequency coefficients.
        """
        N = len(signal)
        if N == 0:
            return np.array([], dtype=np.complex128)

        N_padded = self.next_power_of_2(N)
        if N_padded != N:
            padded_signal = signal.pad(N_padded)
            data = padded_signal.data
        else:
            data = signal.data.copy()
        return self.fft_recursive_dif(data)


    def compute_ifft_dif(self, spectrum):
        """
        Compute IFFT using Radix-2 DIF Cooley-Tukey algorithm.
        Automatically pads input to next power of 2 if necessary.
        Returns: numpy array (time-domain samples).
        """
        N = len(spectrum)
        if N == 0:
            return np.array([], dtype=np.complex128)

        N_padded = self.next_power_of_2(N)
        if N_padded != N:
            padded_spectrum = np.zeros(N_padded, dtype=np.complex128)
            padded_spectrum[:N] = spectrum
            spectrum = padded_spectrum
        else:
            spectrum = np.array(spectrum, dtype=np.complex128)

        x = self.ifft_recursive_dif(spectrum)
        return x / len(spectrum)
      
    def compute_dft(self, signal: DiscreteSignal):  
        return super().compute_dft(signal)  
      
    def compute_idft(self, spectrum):  
        return super().compute_idft(spectrum) 