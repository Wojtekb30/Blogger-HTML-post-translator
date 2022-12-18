# Blogger HTML post translator
It's a program I made for translating Blogger posts. It translates text written in HTML file between "&lt;p>" and "&lt;/p>"s. The translated HTML can be saved to a new HTML or text file.

<b>How to use it?:</b>

1. Download .exe or .py of the translator program.

2. (If you're translating your Blogger post) In post's editor open HTML editor view:
![image](https://user-images.githubusercontent.com/112283903/208311034-db79cc65-fe03-4da7-ace3-a21f65ca8770.png)

3. (If you're translating your Blogger post) Copy the HTML data, paste it into Notepad and save it on your computer as a text (.txt) or HTML (.html):
![image](https://user-images.githubusercontent.com/112283903/208311164-9361beb8-6b82-457a-bd77-9bf8074b2e2b.png)

4. Run the translator program and follow instructions it displays:

5. Type destination language code (for example pl, en, es etc.).

6. Choose and open the text or HTML file you want to translate.
![image](https://user-images.githubusercontent.com/112283903/208311268-96042906-67ac-4bba-85cb-f2cd36027ec7.png)

7. Wait for the program to finish.

8. When it finishes, save the result, then press ENTER/RETURN to close the program.

9. Use the new HTML. If you're using Blogger - open the translated file in Notepad and paste it into HTML editor view of a new Blogger post. Preview if it works and looks well.
![image](https://user-images.githubusercontent.com/112283903/208311523-a6fb65d8-ff18-48e4-8411-1a1db35e1a1f.png)
![image](https://user-images.githubusercontent.com/112283903/208311377-5450d766-b66c-4135-ae9e-32bd2b6775b4.png)

<b>How it works and troubleshooting:</b>

The program scans text of chosen file until it finds "&lt;p>". It then sends text until "&lt;/p>" to the translator (Python googletrans library). After translating, the text it puts the translated text back into the document where the original would be. It repeats until it reads (and translates) entire document.

If it doesn't work (and you're running the .py file), you might have to download proper (latest) version of googletrans. To do that use terminal command:

pip3 install googletrans==3.1.0a0

If program freezes for a long time, click inside its terminal window and press ENTER/RETURN.
