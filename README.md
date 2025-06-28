# 🎬 SubShift

**SubShift** is a lightweight desktop application for easily adjusting the timing of `.srt` subtitle files.  
With a clean graphical interface and support for any file encoding, SubShift lets you shift subtitle timings forward or backward in precise 0.1 second steps — ideal for syncing subtitles with videos that are just slightly out of sync.

---

## 🚀 Features

- ⏱️ Shift subtitle timings forward or backward by 0.1-second increments
- 🌍 Supports any file encoding automatically (via `chardet`)
- 🧾 Preserve original formatting and encoding
- 💾 Choose to overwrite the original file or save as a new one
- 🖱️ Simple and clean GUI — no technical skills required
- 🔒 Safe processing — never modifies non-timing lines

---

## 🖼️ Interface Preview

![image](https://github.com/user-attachments/assets/f79b6780-d2bc-48c3-a548-a21737754311)


---

## 🛠️ Installation

### Requirements

- Python 3.7+
- [chardet](https://pypi.org/project/chardet/)

### Install chardet

```bash
pip install chardet
```

---

## ▶️ Usage

1. Clone or download the repository
2. Run the app:

```bash
python subshift.py
```

3. Choose your `.srt` file
4. Select the time shift (positive or negative)
5. Choose whether to overwrite or create a new file
6. Click **"Apply change"** and you're done!

---

## 🧠 Why use SubShift?

Sometimes, video and subtitle files aren't perfectly synced — just a few seconds off. Instead of editing timestamps manually or using complex tools, **SubShift** makes the process effortless with a friendly interface and reliable subtitle parsing.

---

## 📁 Example Output

If your original file is `movie.srt`, and you choose **not** to overwrite, the result will be:

```
movie_adjusted.srt
```

---

## 📜 License

MIT License — free for personal and commercial use.

---

## 🤝 Contributing

Want to improve SubShift? Feel free to fork and submit a pull request! Suggestions and bug reports are always welcome.

---

## ❤️ Credits

- Built with [`tkinter`](https://docs.python.org/3/library/tkinter.html) for GUI
- Uses [`chardet`](https://github.com/chardet/chardet) to detect file encoding

---

## 📧 Contact

Created by @foliveross
If you enjoy this tool, feel free to ⭐️ the repo or share it with others!
