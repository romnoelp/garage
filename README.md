# 🚀 Garage: A PyQt6 Inheritance Showcase

Welcome to **Garage**, a **Python PyQt6 application** demonstrating **single and multiple inheritance** through real-world motorcycle models like the **Honda Rebel 1100** and **Honda ADV 160**.

---

## 📌 Features
✅ **Modern GUI** built with **PyQt6**  
✅ **OOP Inheritance Implementation** (Single & Multiple Inheritance)  
✅ **Switchable Transmission** (Honda Rebel 1100: DCT ↔ Manual)  
✅ **Motorcycle Details Window** with **Image & Features**  
✅ **Back Navigation** to the Main Menu  

---

## 📂 Project Structure
```
📦 Garage
│── 📂 Base                # Base Motorcycle Class
│   └── motorcycle.py
│── 📂 Base_Types          # Transmission Types
│   ├── automatic.py
│   └── manual.py
│── 📂 Implementation      # Specific Motorcycle Models
│   ├── adv.py
│   └── honda_rebel.py
│── 📂 UI                  # PyQt6 UI Files
│   ├── main_menu.py
│   ├── detail_window.py
│── 📂 Images              # Motorcycle Images
│   ├── adv.jpg
│   ├── rebel.jpg
│── main.py                # Entry Point
│── styles.qss             # Stylesheet for UI
│── README.md              # This file
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone git@github.com:romnoelp/garage.git
cd garage
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install PyQt6 requests
```

### 4️⃣ Run the Application
```bash
python main.py
```

---

## 🖥️ How It Works
1️⃣ **Select a motorcycle** (Honda Rebel 1100 or Honda ADV 160) from the main menu.  
2️⃣ A **detailed window opens** showing **motorcycle specs & an image**.  
3️⃣ **For Honda Rebel 1100**, you can **switch transmission** (DCT ↔ Manual).  
4️⃣ Click **Back** to return to the main menu.  

---


## 📜 License
This project is **open-source** and available under the **MIT License**.  

---

