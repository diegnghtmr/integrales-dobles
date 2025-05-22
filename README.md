# 📐 Double Integral Calculator with 3D Visualization 📊

Welcome to the Double Integral Calculator repository! This project allows you to calculate the volume under a surface (defined by a function z = f(x, y)) using Riemann sums and visualize both the surface and the approximating prisms in 3D. A great tool to better understand multivariable calculus! 🚀

Developed by: Diego Flores and Juan Pablo Mora.

## 🌟 Key Features

This project offers a set of interactive tools to explore double integrals:

* **User-Friendly Graphical User Interface (GUI) 🖼️**: Built with Tkinter for easy interaction.
* **Selection of Predefined Functions 𝑓(𝑥,𝑦)**:
    * z = x + y
    * z = x² + y²
    * z = sin(x) cos(y)
* **Customizable Integration Limits 📏**: Define the intervals [xmin, xmax] and [ymin, ymax].
* **Adjustable Number of Partitions 🔢**: Control the approximation's precision by specifying nx and ny.
* **Multiple Riemann Sum Methods**:
    * Left Endpoint Sum
    * Right Endpoint Sum
    * Midpoint Sum
* **Approximate Volume Calculation 🧱**: Get the numerical value of the volume under the surface.
* **Interactive 3D Visualization 🌐**:
    * Plot of the surface z = f(x,y).
    * Representation of the rectangular prisms used in the Riemann sum.
    * Labels with the volume of each individual prism in the partition graph.
* **Error Handling ✅**: Input validation to ensure parameters are correct (e.g., xmax > xmin).

## 🛠️ Tech Stack and Dependencies

This project is built entirely in Python and leverages the following libraries:

* **Python 3** 🐍: The main programming language.
* **Tkinter**: For the graphical user interface (usually comes with Python).
* **NumPy**: For efficient numerical calculations and array manipulation.
* **Matplotlib**: For generating 2D and 3D visualizations.

## 📋 Prerequisites

Ensure you have the following software installed on your development machine:

* **Python 3**: The latest stable version is recommended. You can download it from [python.org](https://www.python.org/).
* **pip**: The Python package manager (usually installed with Python).
* **Git**: To clone the repository. You can download it from [git-scm.com](https://git-scm.com/).
* (Optional but recommended) A virtual environment (like `venv` or `conda`) to manage project dependencies. The `.idea/misc.xml` file suggests the use of Miniconda.

## 🚀 Installation and Setup

Follow these steps to get the project running on your local machine:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/diegnghtmr/integrales-dobles.git
    cd integrales-dobles
    ```

2.  **Create and activate a virtual environment** (recommended):
    * Using `venv`:
        ```bash
        python -m venv env
        source env/bin/activate  # On Linux/macOS
        .\env\Scripts\activate   # On Windows
        ```
    * If using Conda:
        ```bash
        conda create -n integrales_env python=3
        conda activate integrales_env
        ```

3.  **Install dependencies**:
    ```bash
    pip install numpy matplotlib
    ```

## 🏃‍♀️ Running the Application

Once you have installed the dependencies, you can run the application:

1.  Ensure you are in the project's root directory (where the `models` folder is located).
2.  Run the `integrales.py` script:
    ```bash
    python models/integrales.py
    ```
    This should open the GUI window where you can interact with the calculator.

## 🧠 How It Works

The core of the calculation lies in the `calcular_volumen_riemann` function. This function takes the mathematical function f(x,y), the integration limits, and the number of partitions (nx, ny) as input. It then divides the integration region into nx * ny rectangles.

For each rectangle, it selects a point (xi, yj) according to the chosen method (left, right, or midpoint). The volume of the prism above this rectangle is f(xi, yj) * dx * dy. The sum of the volumes of all these prisms gives the approximation of the total volume under the surface.

Visualizations are generated using Matplotlib:
* A 3D surface plot shows the shape of f(x,y).
* A second 3D plot shows the rectangular prisms, helping to visualize how the Riemann sum approximates the volume.

## 🤝 Contributions

Contributions are welcome! If you have ideas for improving the tool, new features to add, or find any bugs, feel free to:

1.  **Fork** the project.
2.  Create your **Feature Branch** (`git checkout -b feature/AmazingFeature`).
3.  **Commit** your changes (`git commit -m 'Add some AmazingFeature'`).
4.  **Push** to the branch (`git push origin feature/AmazingFeature`).
5.  Open a **Pull Request**.

You can also simply open an *issue* with the "enhancement" or "bug" tag. Don't forget to give the project a star if you found it useful! ⭐
