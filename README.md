<h1>404Crypt Ransomware</h1>
<h1>By the1%</h1>

The Ransomware is 100% Written in Python language
> Watch the Tutorial to Fully Understanding the Working of the 404Crypt Ransomware
YouTube Tutorial: https://www.youtube.com/

> <h1>DISCLAIMER</h1>
> <h5>This Tool Should Only Be Used For Educational & Cryptographical & Testing Purposes . Not for Revenge or Causing Harm</h5>
> <h5><br><br>Misuse or Illegal Usage of the Tool One will Be solely Be held Responsible for not Obeying Federal & State Laws</h5>
> <h5><br><br>The1% shall not assume any responsibility for Misuse or Damage Caused by the Program</h5>

<h5>Run the RSA_KEY_PAIR file to generate Asymmetric Keys Required For Key Encrpytion</h5>
<h4>For the Decryption to Take Place Place the Key On the Desktop of The Target System so as to Decrypt The Files</h4>

<h4>Files tha Make-up the Ransomware</h4>
<li><b>Ransom_Note.py</b></li>
    <ol>
    <h4>This is Designed Based on Tkinter Libray to act as Display Ransom Note after Files are Encrypted</h4>
    <h4>It Displays Prompts to the Victim About What is actually happening on their System</h4>
    <h4>The Ransom Note Initiates a CountDown Timer on the Target System</h4>
    <h6>Once Payments aren't Done Within the Period Of the Timer, All Files Encrypted are shredded | Deleted Permanently</h6>
    <h6>Even Just Run Once the Timer is Done Files in the Location Specified are Deleted [TAKE NOTE]</h6>
    </ol>

<li><b>RSA_KEY_PAIR_GEN.py</b></li> 
    <ol>
    <h4>This implements RSA to generate private & Public Key pairs that are used for encryption of the symmetric KEy used for system files Encryption</h4>
    <h6>For Consistency This Should Be run Once </h6>
    <h4>The AES symmetric Key used in Encryption is encrypted using Attackers Public key</h4>
    <h4>Such that only the Attacker using their Private key can decrypt the files on the Target System</h4>
    </ol>

<li><b>Encrypt.py</b></li> 
    <ol>
    <h4>This file is The basis of the Program, Based on the OS Detection, File extensions specified, it Encrypts all users files on the Target System Utilizing much CPU Power to ensure faster Operations</h4>
    <h4>Whenever the Program is run it generates a Random AES key for encryption of the Target system</h4>
    <h6>When The Encryption Process is Complete .. the random AES key used for Encryption of the System is also Encrypted using the Attacker's Public Key then Automatically Emailed To the Attacker via Gmail</h6>
    <h4>This means only the Attacker Can Decrypt the Encrypted key received via mail using their private key copy</h4>
    <h4>Once the all Files are Encrypted using the <b>Ransom_Note.py Module</b> The Ransom Note is Displayed onto the Victim's Screen</h4>
    <h6>for Encryption to Start, the symmetric.pem & The public key in public.pem File Should be in the Same Wording Dir</h6>
    </ol>

<li><b>Key_Decrypt.py</b></li> 
    <ol>
    <h6>This file is Retained by the Attacker</h6>
    <h4>When The Encrypted AES symmetric key symmetric.pem is received by the Attacker by Mail</h4>
    <h4>Once the symmetric.pem file is placed in the same Working Directory as the File Using the Attacker's Private key it can be Decrypted so that to Wait for the Ransom From the Victim</h4>
    <h6>The symmetric AES key symmetric.pem and the RSA asymmetric private Key private.pem Should Be kept in the same working directory as Key_Decrypt.py File</h6>
    </ol>

<li><b>Email_Me.py</b></li> 
    <ol>
    <h4>Once this File is Run With an Active Internet Connection ... It Communicates Back to the Attacker</h4>
    <h4>It Sends a Copy of the Encrypted symmetric AES key stored in symmetric.pem file to the Attacker[BOSS] Via Mail</h4>
    </ol>
<li><b>Decrypt.py</b></li> 
    <ol>
    <h5>This is Decryption System File  </h5>
    <h4>This is Derived as Child Class of Malicious class in the Encrypt.py Module</h4>
    <h4>Once the Unencrypted Authentic AES key symmetric.pem File is placed in the Current Directory as the Decrypt.py File</h4>
    <h4>All Encrypted Files Will Be Decrypted </h4>
    </ol>
