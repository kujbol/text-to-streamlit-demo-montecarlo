
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calculate_pi(num_points):
    points = np.random.rand(num_points, 2)
    inside_circle = points[np.linalg.norm(points, axis=1) <= 1]
    pi = 4 * len(inside_circle) / num_points
    return pi, points, inside_circle

def plot_points(points, inside_circle):
    plt.figure(figsize=(6, 6))
    plt.scatter(points[:, 0], points[:, 1], color='blue', alpha=0.5, label='Outside Circle')
    plt.scatter(inside_circle[:, 0], inside_circle[:, 1], color='red', alpha=0.5, label='Inside Circle')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    st.pyplot()

def main():
    st.title("Monte Carlo Pi Calculator")
    num_points = st.number_input("Number of Points", min_value=1, step=1, value=1000)
    if st.button("Calculate"):
        pi, points, inside_circle = calculate_pi(num_points)
        st.write(f"Approximated Pi: {pi}")
        plot_points(points, inside_circle)

if __name__ == '__main__':
    main()
