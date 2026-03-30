from unittest import result
import numpy as np
import matplotlib.pyplot as plt

from nfsl.using_class import INF

# Todo: Define Signal class
class Signal:
    def __init__(self, INF):
        # Initialize
        self.INF = INF
        self.signal = np.zeros(2 * (INF) + 1)

    def set_value_at_time(self, t, value):
        # Set the value at time index t
        if -self.INF <= t <= self.INF :
            self.signal[t + self.INF] = value

    def shift(self, k):
        shifted_signal = Signal(self.INF)
        for n in range(-self.INF, self.INF + 1):
            if -self.INF <= n - k <= self.INF:
                shifted_signal.signal[n + self.INF] = self.signal[n - k + self.INF]
        return shifted_signal

    def add(self, other):
        # Add two signals and return the resultant signal
        resultant = Signal(self.INF)
        resultant.signal = self.signal + other.signal
        return resultant

    def multiply(self, scalar):
        # Multiply a constant value with the signal
        answer = Signal(self.INF)
        answer.signal = scalar * self.signal
        return answer
    
    def multiply_signals(self, other):
        # Multiply two signals element-wise, handling different INF values
        min_INF = min(self.INF, other.INF)
        result = Signal(min_INF)
    
        for n in range(-min_INF, min_INF + 1):
            # Check if index is valid for both signals
            if -self.INF <= n <= self.INF and -other.INF <= n <= other.INF:
                result.signal[n + min_INF] = (self.signal[n + self.INF] * 
                                          other.signal[n + other.INF])    
        return result
    
    def is_causal(self):
        """Check if the system is causal (h[n] = 0 for n < 0)"""
        for n in range(-self.impulse_response.INF, 0):
            if abs(self.impulse_response.signal[n + self.impulse_response.INF]) > 1e-10:
                return False
        return True
    def is_stable(self):
        """Check if the system is BIBO stable (sum of |h[n]| is finite)"""
        total = np.sum(np.abs(self.impulse_response.signal))
        return np.isfinite(total)

    def is_memoryless(self):
        """Check if system is memoryless (h[n] = 0 for all n != 0)"""
        for n in range(-self.impulse_response.INF, self.impulse_response.INF + 1):
            if n != 0 and abs(self.impulse_response.signal[n + self.impulse_response.INF]) > 1e-10:
                return False
        return True
    
    def plot(self, title="Discrete Signal"):
        # Plot the signal
        plt.figure(figsize=(10, 6))
        plt.stem(range(-self.INF, self.INF + 1), self.signal)
        #plt.stem(range(-self.INF, self.INF + 1), self.shift(15).signal, linefmt='r-', markerfmt='ro', basefmt=' ')
        #plt.stem(range(-self.INF, self.INF + 1), self.multiply(2).signal, linefmt='g-', markerfmt='go', basefmt=' ')
        plt.title(title)
        plt.xlabel("n")
        plt.ylabel("x(n)")
        plt.grid(True)
        plt.show()


class SuperSignal:
    def __init__(self):
        self.components = []

    def add(self, signal: Signal, coefficient=1.0):
        self.components.append((coefficient, signal))

        
# Todo: Define LTI class
class LTI_System:
    def __init__(self, impulse_response: Signal):
        # Initialize
        self.impulse_response = impulse_response

    def linear_combination_of_impulses(self, input_signal: Signal):
        # Decompose the signal into impulses and corresponding coefficients
        coefficients = []
        impulses = []
        
        for n in range(-input_signal.INF, input_signal.INF + 1):
            if input_signal.signal[n + input_signal.INF] != 0:
                coefficients.append(input_signal.signal[n + input_signal.INF])                
                impulse = Signal(input_signal.INF)
                impulse.set_value_at_time(n, 1) # Unit impulse function at position n
                impulses.append(impulse)
        
        return coefficients, impulses

    def output(self, input_signal: Signal):
        coefficients, impulses = self.linear_combination_of_impulses(input_signal)
        output_signal = Signal(input_signal.INF)
        
        for i in range(len(coefficients)):
            if coefficients[i] != 0:
                k_index = -input_signal.INF
                count = 0
                for n in range(-input_signal.INF, input_signal.INF + 1):
                    if input_signal.signal[n + input_signal.INF] != 0:
                        if count == i:
                            k_index = n
                            break
                        count += 1
            
                shifted_h = self.impulse_response.shift(k_index) # Shifting h(n) by k_index to adjust the zero position           
                scaled = shifted_h.multiply(coefficients[i]) # Later add to the convolution sum
                output_signal = output_signal.add(scaled)
        
        return output_signal
    
    def output_super(self, super_signal: SuperSignal):
        output_signal = Signal(super_signal.components[0][1].INF)
        
        for coefficient, signal in super_signal.components:
            temp_output = self.output(signal)
            scaled_output = temp_output.multiply(coefficient)
            output_signal = output_signal.add(scaled_output)
        
        return output_signal
    
    def circular_convolution(self, input_signal: Signal, period):
        """Perform circular convolution with given period"""
        output_signal = Signal(input_signal.INF)
    
        for n in range(period):
            sum_val = 0
            for k in range(period):
                h_idx = (n - k) % period
                if -input_signal.INF <= k <= input_signal.INF and -self.impulse_response.INF <= h_idx <= self.impulse_response.INF:
                    sum_val += input_signal.signal[k + input_signal.INF] * self.impulse_response.signal[h_idx + self.impulse_response.INF]
            output_signal.set_value_at_time(n, sum_val)
    
        return output_signal
    
    def step_response(self):
        """Compute step response: output when input is unit step u[n]"""
        INF = self.impulse_response.INF
        unit_step = Signal(INF)
        for n in range(0, INF + 1):
            unit_step.set_value_at_time(n, 1)

        return self.output(unit_step)
    def impulse_response_output(self):
        """Return the impulse response itself (output to unit impulse)"""
        return self.impulse_response

    def ramp_response(self):
        """Compute response to ramp input r[n] = n*u[n]"""
        INF = self.impulse_response.INF
        ramp = Signal(INF)
        for n in range(0, INF + 1):
            ramp.set_value_at_time(n, n)

        return self.output(ramp)
    
    def inverse_system(self):
        """
        Find inverse system (if it exists)
        For simple cases: if h[0] != 0, approximate inverse
        """
        INF = self.impulse_response.INF
        h_inv = Signal(INF)
    
        # Simple case: if h is [h0, h1, h2, ...], find inverse
        h0 = self.impulse_response.signal[self.impulse_response.INF]
    
        if abs(h0) < 1e-10:
            raise ValueError("Cannot invert: h[0] = 0")
    
        h_inv.set_value_at_time(0, 1.0 / h0)
    
        # For FIR, compute inverse coefficients iteratively
        for n in range(1, INF + 1):
            sum_val = 0
            for k in range(1, n + 1):
                if -INF <= n - k <= INF:
                    h_val = self.impulse_response.signal[k + self.impulse_response.INF]
                    h_inv_val = h_inv.signal[n - k + h_inv.INF]
                    sum_val += h_val * h_inv_val
        
            h_inv.set_value_at_time(n, -sum_val / h0)
    
        return LTI_System(h_inv)
    
    def dc_gain(self):
        """Compute DC gain: H(0) = sum of all h[n]"""
        return np.sum(self.impulse_response.signal)

    def system_gain_at_frequency(self, omega):
        """Compute gain at specific frequency ω"""
        gain = 0
        for n in range(-self.impulse_response.INF, self.impulse_response.INF + 1):
            h_n = self.impulse_response.signal[n + self.impulse_response.INF]
            gain += h_n * np.exp(-1j * omega * n)
        return gain

    def impulse_response_energy(self):
        """Compute energy of impulse response"""
        return np.sum(self.impulse_response.signal ** 2)
    
    def compare_with(self, other, test_signal: Signal):
        """Compare two systems using a test signal"""
        y1 = self.output(test_signal)
        y2 = other.output(test_signal)
    
        # Compute error metrics
        mse = np.mean((y1.signal - y2.signal) ** 2)
        max_error = np.max(np.abs(y1.signal - y2.signal))
    
        print(f"Mean Squared Error: {mse}")
        print(f"Maximum Error: {max_error}")
    
        # Plot comparison
        plt.figure(figsize=(12, 4))
        plt.stem(range(-test_signal.INF, test_signal.INF + 1), 
             y1.signal, linefmt='b-', markerfmt='bo', label='System 1')
        plt.stem(range(-test_signal.INF, test_signal.INF + 1), 
             y2.signal, linefmt='r--', markerfmt='ro', label='System 2')
        plt.legend()
        plt.title("System Comparison")
        plt.grid(True)
        plt.show()
    
        return mse, max_error
    
    def output_periodic(self, one_period: Signal, period_length, num_periods=3):
        """
        Compute output when input is periodic
        one_period: one period of the signal
        period_length: length of one period
            num_periods: how many periods to compute
        """
        INF = one_period.INF * num_periods
        periodic_input = Signal(INF)
    
        # Repeat the signal
        for p in range(-num_periods, num_periods + 1):
            for n in range(-one_period.INF, one_period.INF + 1):
                shifted_n = n + p * period_length
                if -INF <= shifted_n <= INF:
                    periodic_input.set_value_at_time(
                        shifted_n, 
                        one_period.signal[n + one_period.INF]
                    )
    
        return self.output(periodic_input)
    
    def get_system_delay(self):
        """
        Find the delay of the system (where impulse response peaks or starts)
        Returns the time index of maximum magnitude
        """
        max_idx = np.argmax(np.abs(self.impulse_response.signal))
        delay = max_idx - self.impulse_response.INF
        return delay

    def is_zero_delay(self):
        """Check if system has zero delay (peak at n=0)"""
        return self.get_system_delay() == 0
    
    def decompose_even_odd(self):
        """
        Decompose impulse response into even and odd parts
        h_e[n] = (h[n] + h[-n]) / 2
        h_o[n] = (h[n] - h[-n]) / 2
        """
        INF = self.impulse_response.INF
        h_even = Signal(INF)
        h_odd = Signal(INF)
    
        for n in range(-INF, INF + 1):
            h_n = self.impulse_response.signal[n + INF]
            h_minus_n = self.impulse_response.signal[-n + INF]
        
            h_even.set_value_at_time(n, (h_n + h_minus_n) / 2)
            h_odd.set_value_at_time(n, (h_n - h_minus_n) / 2)
    
        return LTI_System(h_even), LTI_System(h_odd)
    
    def is_accumulator(self):
        """
        Check if system is an accumulator: y[n] = sum_{k=-inf}^{n} x[k]
        Impulse response: h[n] = u[n] (unit step)
        """
        # Check if h[n] = 1 for n >= 0 and 0 for n < 0
        for n in range(-self.impulse_response.INF, 0):
            if abs(self.impulse_response.signal[n + self.impulse_response.INF]) > 1e-10:
                return False
    
        for n in range(0, self.impulse_response.INF + 1):
            if abs(self.impulse_response.signal[n + self.impulse_response.INF] - 1) > 1e-10:
                return False
    
        return True

    def is_differentiator(self):
        """
        Check if system is a first-difference: y[n] = x[n] - x[n-1]
        Impulse response: h[0] = 1, h[1] = -1
        """
        if abs(self.impulse_response.signal[0 + self.impulse_response.INF] - 1) > 1e-10:
            return False
        if abs(self.impulse_response.signal[1 + self.impulse_response.INF] + 1) > 1e-10:
            return False
    
        # Check all other values are zero
        for n in range(-self.impulse_response.INF, self.impulse_response.INF + 1):
            if n not in [0, 1]:
                if abs(self.impulse_response.signal[n + self.impulse_response.INF]) > 1e-10:
                    return False

        return True
    
    def is_linear_phase(self):
        """
        Check if system has linear phase (symmetric or antisymmetric impulse response)
        Type I: h[n] = h[N-n] (even length, symmetric)
        Type II: h[n] = -h[N-n] (even length, antisymmetric)
        """
        # Check symmetry
        is_symmetric = True
        is_antisymmetric = True
    
        for n in range(-self.impulse_response.INF, self.impulse_response.INF + 1):
            h_n = self.impulse_response.signal[n + self.impulse_response.INF]
            h_minus_n = self.impulse_response.signal[-n + self.impulse_response.INF]
        
            if abs(h_n - h_minus_n) > 1e-10:
                is_symmetric = False
            if abs(h_n + h_minus_n) > 1e-10:
                is_antisymmetric = False
    
        return is_symmetric or is_antisymmetric
    
    def normalize_dc_gain(self):
        """
        Normalize system so DC gain = 1
        Returns new system with h_norm[n] = h[n] / (sum of h[n])
        """
        dc_gain = self.dc_gain()
    
        if abs(dc_gain) < 1e-10:
            raise ValueError("Cannot normalize: DC gain is zero")

        normalized_h = self.impulse_response.multiply(1.0 / dc_gain)
        return LTI_System(normalized_h)
    
    def scale_impulse_response(self, scale_factor):
        """Scale the impulse response by a constant"""
        scaled_h = self.impulse_response.multiply(scale_factor)
        return LTI_System(scaled_h)
    
    def overshoot(self):
        """
        Calculate overshoot in step response
        Overshoot = (peak - final_value) / final_value * 100%
        """
        step_resp = self.step_response()
        final_value = step_resp.signal[-1]
        peak_value = np.max(step_resp.signal)
    
        if abs(final_value) < 1e-10:
            return None
    
        overshoot_percent = (peak_value - final_value) / abs(final_value) * 100
        return overshoot_percent
    
    def output_energy_from_input_energy(self, input_energy):
        """
        Calculate output energy given input energy
        For deterministic signals: E_y ≤ E_x * (sum of |h[n]|)^2
        """
        h_sum_squared = (np.sum(np.abs(self.impulse_response.signal))) ** 2
        max_output_energy = input_energy * h_sum_squared
    
        return max_output_energy

    def energy_amplification_factor(self):
        """
        Maximum factor by which system can amplify signal energy
        """
        return (np.sum(np.abs(self.impulse_response.signal))) ** 2
    
    

def correlate(signal1: Signal, signal2: Signal):
    """Compute cross-correlation of two signals"""
    # Maximum possible lag where signals can overlap
    max_lag = signal1.INF + signal2.INF
    corr = Signal(max_lag)
    
    for lag in range(-max_lag, max_lag + 1):
        sum_val = 0
        for n in range(-signal1.INF, signal1.INF + 1):
            # Check if n+lag is within signal2's range
            if -signal2.INF <= n + lag <= signal2.INF:
                sum_val += (signal1.signal[n + signal1.INF] * 
                           signal2.signal[n + lag + signal2.INF])
        corr.set_value_at_time(lag, sum_val)
    
    return corr

def auto_correlation(signal: Signal):
    """Compute auto-correlation of a signal"""
    return correlate(signal, signal)


def estimate_impulse_response(input_signal: Signal, output_signal: Signal):
    """Estimate impulse response given input and output"""
    # Using deconvolution approach
    # This is a simplified version - real deconvolution is more complex
    
    INF = max(input_signal.INF, output_signal.INF)
    estimated_h = Signal(INF)
    
    # Find first non-zero input value
    first_nonzero_idx = None
    for n in range(-INF, INF + 1):
        if abs(input_signal.signal[n + INF]) > 1e-10:
            first_nonzero_idx = n
            break
    
    if first_nonzero_idx is not None:
        input_val = input_signal.signal[first_nonzero_idx + INF]
        for n in range(-INF, INF + 1):
            output_val = output_signal.signal[n + INF]
            estimated_h.set_value_at_time(n - first_nonzero_idx, output_val / input_val)
    
    return estimated_h

def cascade_systems(system1: LTI_System, system2: LTI_System):
    """Cascade two LTI systems - convolve their impulse responses"""
    INF = max(system1.impulse_response.INF, system2.impulse_response.INF)
    combined_h = Signal(2 * INF)
    
    # Convolve h1 and h2
    for n in range(-2*INF, 2*INF + 1):
        sum_val = 0
        for k in range(-INF, INF + 1):
            if -INF <= n - k <= INF:
                h1_val = system1.impulse_response.signal[k + system1.impulse_response.INF]
                h2_val = system2.impulse_response.signal[n - k + system2.impulse_response.INF]
                sum_val += h1_val * h2_val
        if -combined_h.INF <= n <= combined_h.INF:
            combined_h.set_value_at_time(n, sum_val)
    
    return LTI_System(combined_h)

def parallel_systems(system1: LTI_System, system2: LTI_System):
    """Combine two LTI systems in parallel - add their impulse responses"""
    INF = max(system1.impulse_response.INF, system2.impulse_response.INF)
    combined_h = system1.impulse_response.add(system2.impulse_response)
    return LTI_System(combined_h)

def create_edge_detector(INF):
    """Create a simple edge detection filter"""
    h = Signal(INF)
    h.set_value_at_time(-1, -1)
    h.set_value_at_time(0, 0)
    h.set_value_at_time(1, 1)
    return h

# Usage
# edge_system = LTI_System(create_edge_detector(INF))
# edges = edge_system.output(input_signal)
# edges.plot("Edge Detection Output")


def create_lowpass_filter(INF, cutoff_length=5):
    """Create a simple low-pass filter"""
    h = Signal(INF)
    for n in range(-cutoff_length//2, cutoff_length//2 + 1):
        h.set_value_at_time(n, 1.0/cutoff_length)
    return h

def create_highpass_filter(INF):
    """Create high-pass filter using delta minus low-pass"""
    lowpass = create_lowpass_filter(INF)
    delta = Signal(INF)
    delta.set_value_at_time(0, 1)
    
    highpass = Signal(INF)
    for n in range(-INF, INF + 1):
        highpass.signal[n + INF] = (delta.signal[n + INF] - 
                                    lowpass.signal[n + INF])
    return highpass

def matched_filter_detection(template: Signal, noisy_signal: Signal):
    """Detect template signal in noisy signal using matched filtering"""
    # Matched filter is time-reversed template
    matched_h = Signal(template.INF)
    for n in range(-template.INF, template.INF + 1):
        matched_h.set_value_at_time(n, template.signal[-n + template.INF])
    
    system = LTI_System(matched_h)
    detection_output = system.output(noisy_signal)
    
    # Find peak
    max_val = np.max(np.abs(detection_output.signal))
    max_idx = np.argmax(np.abs(detection_output.signal))
    detected_position = max_idx - detection_output.INF
    
    return detection_output, detected_position, max_val

def create_system_from_difference_equation(a_coeffs, b_coeffs, INF):
    """
    Create system from difference equation:
    a[0]*y[n] + a[1]*y[n-1] + ... = b[0]*x[n] + b[1]*x[n-1] + ...
    """
    # For FIR systems (a[0]=1, rest are 0)
    h = Signal(INF)
    for i, b in enumerate(b_coeffs):
        h.set_value_at_time(i, b / a_coeffs[0])
    return h

# Example: y[n] = 0.5*x[n] + 0.3*x[n-1] + 0.2*x[n-2]
h = create_system_from_difference_equation([1], [0.5, 0.3, 0.2], INF)

def signal_energy(signal: Signal):
    """Calculate signal energy"""
    return np.sum(signal.signal ** 2)

def signal_power(signal: Signal, N):
    """Calculate average power over N samples"""
    return signal_energy(signal) / (2*N + 1)

def convolution_energy_theorem(x: Signal, h: Signal, y: Signal):
    """Verify: Energy(y) = Energy(x) * sum(|h[n]|^2)"""
    Ex = signal_energy(x)
    Eh = np.sum(h.signal ** 2)
    Ey = signal_energy(y)
    
    print(f"Energy of input: {Ex}")
    print(f"Energy of impulse response: {Eh}")
    print(f"Energy of output: {Ey}")
    print(f"Ex * Eh = {Ex * Eh}")
    print(f"Ratio Ey/(Ex*Eh) = {Ey/(Ex*Eh) if Ex*Eh != 0 else 'undefined'}")


if __name__ == "__main__":
    INF = 10

    # Component signals
    x1 = Signal(INF)
    x1.set_value_at_time(0, 1)

    x2 = Signal(INF)
    x2.set_value_at_time(2, 1)

    # Todo: Create SuperSignal: x(n) = 2*x1(n) - x2(n)
    super_x = SuperSignal()
    super_x.add(x1, coefficient=2)
    super_x.add(x2, coefficient=-1)
    # Impulse response
    h = Signal(INF)
    h.set_value_at_time(0, 1)
    h.set_value_at_time(1, 0.5)

    system = LTI_System(h)

    # Todo: Output using superposition
    y = system.output_super(super_x)
    y.plot("Output Signal y(n) using Superposition")

