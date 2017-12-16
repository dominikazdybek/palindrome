# palindrome

This repository consists of three files that contain the solution to the problem of returning the largest number-palindrome, which is the product of two prime five-digit numbers and returns the multipliers themselves. The code is written in Python language. 

#### The algorithm for executing each program consists of the following stages:
* generating list of the prime numbers (there was no way to optimalize this step, because there is no algorithm to find prime numbers)
* multiplying the numbers from the created list (each with each one) and checking if the multiplication result is a palindrome
* tenfold measurement of algorithm execution time in each of the files (that was my way to check which of the proposed algorithms is the fastest)

#### The average execution time of the algorithm in each file was:
* **solution1.py** - 98,601s
* **solution2.py** - 720,583s
* **solution3.py** - 190,940s

The largest number-palindrome is `999949999`. It is the product of two prime five-digit numbers: `30109` and `33211`.

#### Calculations were made on a computer with parameters:
* Memory : 8 GiB
* Processor : Intel® Core™ i5-6200U CPU @ 2.30GHz × 4
* OS : ubuntu 17.04
* Python : 3.5.3
