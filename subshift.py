import tkinter as tk
from tkinter import filedialog, messagebox
import re
import chardet
import os

def detect_encoding(filepath):
    with open(filepath, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding'] or 'utf-8'

def time_to_ms(time_str):
    hours, minutes, seconds = time_str.split(':')
    seconds, milliseconds = seconds.split(',')
    total_ms = (
        int(hours) * 3600000 +
        int(minutes) * 60000 +
        int(seconds) * 1000 +
        int(milliseconds)
    )
    return total_ms

def ms_to_time(ms):
    hours = ms // 3600000
    ms %= 3600000
    minutes = ms // 60000
    ms %= 60000
    seconds = ms // 1000
    milliseconds = ms % 1000
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def adjust_time_line(line, offset_ms):
    pattern = r'(\d{2}:\d{2}:\d{2},\d{3})\s-->\s(\d{2}:\d{2}:\d{2},\d{3})'
    match = re.match(pattern, line)
    if not match:
        return line

    start, end = match.groups()
    new_start = max(0, time_to_ms(start) + offset_ms)
    new_end = max(0, time_to_ms(end) + offset_ms)
    return f"{ms_to_time(new_start)} --> {ms_to_time(new_end)}"

def adjust_subtitles(filepath, offset, overwrite):
    encoding = detect_encoding(filepath)
    offset_ms = int(offset * 1000)

    with open(filepath, 'r', encoding=encoding) as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_line = adjust_time_line(line.strip(), offset_ms)
        new_lines.append(new_line + '\n')

    if overwrite:
        output_path = filepath
    else:
        base, ext = os.path.splitext(filepath)
        output_path = base + '_adjusted' + ext

    with open(output_path, 'w', encoding=encoding) as f:
        f.writelines(new_lines)

    return output_path

# GUI
class SubtitleApp:
    def __init__(self, root):
        self.root = root
        root.title("Subtitle Timing Adjuster (.SRT)")

        self.filepath = ""

        self.label_file = tk.Label(root, text="Subtitle File:")
        self.label_file.pack()

        self.button_browse = tk.Button(root, text="Choose file", command=self.browse_file)
        self.button_browse.pack()

        self.label_offset = tk.Label(root, text="Timing offset (seconds, can be negative):")
        self.label_offset.pack()

        self.offset_value = tk.DoubleVar(value=0.1)
        self.slider = tk.Scale(root, from_=-5.0, to=5.0, resolution=0.1, orient=tk.HORIZONTAL, variable=self.offset_value, length=300)
        self.slider.pack()

        self.overwrite = tk.BooleanVar()
        self.check_overwrite = tk.Checkbutton(root, text="Overwrite original file", variable=self.overwrite)
        self.check_overwrite.pack()

        self.button_apply = tk.Button(root, text="Apply change", command=self.apply_changes)
        self.button_apply.pack(pady=10)

    def browse_file(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("SRT files", "*.srt")])
        if self.filepath:
            self.label_file.config(text=f"Selected file: {os.path.basename(self.filepath)}")

    def apply_changes(self):
        if not self.filepath:
            messagebox.showerror("Error", "Please select an .srt file first.")
            return

        offset = self.offset_value.get()
        try:
            output_path = adjust_subtitles(self.filepath, offset, self.overwrite.get())
            messagebox.showinfo("Success", f"File saved at:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = SubtitleApp(root)
    root.mainloop()
