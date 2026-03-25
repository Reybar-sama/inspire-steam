import customtkinter as ctk
import psutil
import platform
import shutil

class SystemMonitorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("System Specs & Optimizer")
        self.geometry("450x800")
        ctk.set_appearance_mode("dark")

        # --- Scrollable Container ---
        self.main_container = ctk.CTkScrollableFrame(self)
        self.main_container.pack(fill="both", expand=True, padx=10, pady=10)

        # --- UI Header ---
        self.header_label = ctk.CTkLabel(self.main_container, text="System Monitor", font=("Arial", 24, "bold"))
        self.header_label.pack(pady=20)

        # --- Theme Toggle ---
        self.theme_switch = ctk.CTkSwitch(self.main_container, text="Dark Mode", command=self.toggle_theme)
        self.theme_switch.pack(pady=10)
        self.theme_switch.select()

        # --- Storage Breakdown Section ---
        self.storage_frame = ctk.CTkFrame(self.main_container)
        self.storage_frame.pack(pady=10, padx=10, fill="x")
        
        self.storage_title = ctk.CTkLabel(self.storage_frame, text="Storage Breakdown", font=("Arial", 18, "bold"))
        self.storage_title.pack(pady=10)
        
        self.disk_labels = []
        self.update_disk_info()

        # --- System Drivers Section ---
        self.driver_frame = ctk.CTkFrame(self.main_container)
        self.driver_frame.pack(pady=10, padx=10, fill="x")
        
        self.driver_title = ctk.CTkLabel(self.driver_frame, text="System Drivers", font=("Arial", 18, "bold"))
        self.driver_title.pack(pady=10)

        # Mock driver data (In a real app, you'd use WMI or subprocess to fetch these)
        drivers = [
            ("Graphics Card", "Up to Date", "green"),
            ("Network Adapter", "Update Available", "orange"),
            ("Audio Controller", "Up to Date", "green")
        ]

        for name, status, color in drivers:
            d_label = ctk.CTkLabel(self.driver_frame, text=f"{name}: {status}", text_color=color)
            d_label.pack(pady=2)

        # --- Optimization Tips ---
        self.rec_frame = ctk.CTkFrame(self.main_container)
        self.rec_frame.pack(pady=20, padx=10, fill="x")
        
        self.rec_title = ctk.CTkLabel(self.rec_frame, text="Optimization Tips", font=("Arial", 16, "bold"))
        self.rec_title.pack(pady=5)

        self.tips = ctk.CTkLabel(self.rec_frame, text="• Upgrade to SSD for faster boot\n• Clear temporary system files\n• Disable heavy startup apps", justify="left")
        self.tips.pack(pady=10)

    def update_disk_info(self):
        # Clear old labels
        for label in self.disk_labels:
            label.destroy()
        self.disk_labels = []

        # Get partitions
        partitions = psutil.disk_partitions()
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disk_text = f"{partition.device} ({partition.mountpoint}): {usage.percent}% Used\n({usage.used // (1024**3)}GB / {usage.total // (1024**3)}GB)"
                lbl = ctk.CTkLabel(self.storage_frame, text=disk_text, justify="left")
                lbl.pack(pady=5)
                self.disk_labels.append(lbl)
            except PermissionError:
                continue

    def toggle_theme(self):
        if self.theme_switch.get() == 1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

if __name__ == "__main__":
    app = SystemMonitorApp()
    app.mainloop()