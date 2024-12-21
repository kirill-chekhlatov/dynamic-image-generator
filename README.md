# **Dynamic Text Image Generator**

## 🚀 **Project Overview**

**Dynamic Text Image Generator** is a Python-based application designed to dynamically generate images containing text. The program ensures proper text wrapping, adjusts the image height dynamically, and delivers a clean, structured output image.

This project is part of **my portfolio** and demonstrates my ability to create scalable Python scripts, handle text rendering with image processing libraries, and containerize applications using **Docker**.

---

## 🧠 **Problem it Solves**

When generating text-based images (e.g., quotes, instructions, or educational posters), text often overflows the image boundaries or becomes misaligned.  

This project solves these issues by:
1. **Dynamic Resizing:** Adjusting the image height to fit the text properly.
2. **Automatic Wrapping:** Ensuring the text is wrapped based on image width.
3. **Customization:** Supporting user-defined fonts, font sizes, and output paths.
4. **Scalability with Docker:** Simplifying deployment and execution.

---

## 🛠️ **Technologies Used**

- **Python 3.10.12**
- **Pillow (PIL)** — For image creation and text rendering.
- **Docker** — For containerization and easy deployment.

---

## 📦 **Project Structure**

```
.
├── Dockerfile           # Docker configuration for the project
├── docker-compose.yml   # Docker Compose file
├── requirements.txt     # Python dependencies
├── main.py              # Main script for generating images
├── arial.ttf            # Font file (ensure it's present)
└── README.md            # Documentation
```

---

## ⚙️ **How It Works**

1. The script waits for **user input** and accepts dynamic text input from the console.
2. The text is wrapped automatically to fit the image width.
3. If the text exceeds the default height, the image size adjusts dynamically.
4. The wrapped text is rendered onto the image.
5. The image is saved in the `app/` folder.

---

## 🖥️ **Local Setup**

### 1️⃣ **Prerequisites**
- **Python 3.10.12** installed
- Install dependencies:

```bash
pip install -r requirements.txt
```

### 2️⃣ **Run Locally**

Ensure `arial.ttf` is present in the project directory.

Run the script:
```bash
python main.py
```

### 3️⃣ **Provide Input**
- Enter text into the console.
- Each input generates a new image with the provided text.

### 4️⃣ **Exit**
- Type `exit` to stop the program.

---

## 🐳 **Run with Docker**

### 1️⃣ **Build Docker Image**
Build the Docker image:
```bash
docker-compose build
```

### 2️⃣ **Run Interactively**
Start the container in interactive mode:
```bash
docker-compose run -it image-generator
```

- **`-it`:** Enables interactive mode for user input.  

### 3️⃣ **Provide Input**
- Enter your text in the console.
- Each text input generates an image saved in the `app/` folder.

### 4️⃣ **Exit the Program**
- Type `exit` to stop the program gracefully.

---

## 📂 **Configuration Options**

You can customize the following parameters in `main.py`:
- **text:** Default text to display on the image.
- **font_path:** Path to the font file (`arial.ttf` by default).
- **font_size:** Font size (default is `20`).
- **output_image_path:** File path for the output image and image name.

---

## 📂 **Environment Variables (Optional in Docker Compose)**

- **`FONT_PATH`:** Path to the font file inside the Docker container (`/app/arial.ttf`).

---

## 🎯 **Use Cases**

- **Social Media Content:** Automatically generate shareable quotes.  
- **Educational Material:** Create instructional posters dynamically.  
- **Custom Text Banners:** Generate banners with customized messages.  
- **Scalable Solutions:** Integrate into larger text-to-image workflows.

---

## 👤 **About the Author**

This project is part of **my portfolio** and demonstrates my expertise in:
- Python Development  
- Image Processing with Pillow  
- Containerization with Docker  

Feel free to connect with me on **[GitHub](https://github.com/kirill-chekhlatov)** or reach out for collaboration opportunities!

---

## 🤝 **Contributing**

Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch:  
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:  
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

---

## 🛡️ **License**

This project is licensed under the **Creative Commons Attribution (CC BY) License**.

### ⚖️ **Key Terms:**
- **You are free to:**
   - Share: Copy and redistribute the material in any medium or format.
   - Adapt: Remix, transform, and build upon the material for any purpose, even commercially.
- **Under the following terms:**
   - **Attribution:** You must give appropriate credit to **[Kirill Chekhlatov - https://github.com/kirill-chekhlatov]** as the original author, provide a link to the license, and indicate if changes were made.

For more details, see the full license text: [CC BY License](https://creativecommons.org/licenses/by/4.0/)

---

## 🌟 **Acknowledgments**

- **Pillow (PIL)** — Powerful library for image processing.  
- **Docker** — For simplified deployment and scalability.

---

If you encounter any issues, have suggestions, or want to propose new features, feel free to open an issue on GitHub. 🚀