import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

vectorized_f_to_c = np.vectorize(fahrenheit_to_celsius)
temps_f = np.array([32, 68, 100, 212, 77])
temps_c = vectorized_f_to_c(temps_f)
print("Temperatures in Celsius:", temps_c)

def power_func(base, exp):
    return base ** exp

vectorized_power = np.vectorize(power_func)
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
power_results = vectorized_power(bases, exponents)
print("Power results:", power_results)

A = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
b = np.array([7, 4, 5])
x = np.linalg.solve(A, b)
print("Solution to system of equations:", x)

B = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
c = np.array([12, -5, 15])
I = np.linalg.solve(B, c)
print("Currents in the circuit:", I)

def flip_image(image_array):
    return np.flipud(np.fliplr(image_array))

def add_noise(image_array):
    noise = np.random.randint(0, 50, image_array.shape, dtype=np.uint8)
    return np.clip(image_array + noise, 0, 255)

def brighten_channels(image_array, value=40):
    return np.clip(image_array + value, 0, 255)

def apply_mask(image_array, mask_size=(100, 100)):
    h, w, _ = image_array.shape
    y, x = (h - mask_size[0]) // 2, (w - mask_size[1]) // 2
    image_array[y:y+mask_size[0], x:x+mask_size[1]] = [0, 0, 0]
    return image_array

image = Image.open("images/birds.jpg")
image_array = np.array(image)

flipped_image = flip_image(image_array)
noisy_image = add_noise(image_array)
brightened_image = brighten_channels(image_array)
masked_image = apply_mask(image_array)

Image.fromarray(flipped_image).save("flipped_birds.jpg")
Image.fromarray(noisy_image).save("noisy_birds.jpg")
Image.fromarray(brightened_image).save("brightened_birds.jpg")
Image.fromarray(masked_image).save("masked_birds.jpg")
