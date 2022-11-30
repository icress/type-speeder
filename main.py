from tkinter import *
import time
from threading import Thread
from random import choice

window = Tk()
window.geometry('1200x600')
window.title('Type Speed Tester')

sample_text_list = ['''On the 24th of February, 1815, the look out at Notre Dame de la Garde signalled the three master, the Pharaon from Smyrna, Trieste, and Naples. As usual, a pilot put off immediately, and rounding the Chateau d’If, got on board the vessel between Cape Morgion and Rion island. Immediately, and according to custom, the ramparts of Fort Saint–Jean were covered with spectators; it is always an event at Marseilles for a ship to come into port, especially when this ship, like the Pharaon, has been built, rigged, and laden at the old Phocee docks, and belongs to an owner of the city. The ship drew on and had safely passed the strait, which some volcanic shock has made between the Calasareigne and Jaros islands; had doubled Pomegue, and approached the harbor under topsails, jib, and spanker, but so slowly and sedately that the idlers, with that instinct which is the forerunner of evil, asked one another what misfortune could have happened on board. However, those experienced in navigation saw plainly that if any accident had occurred, it was not to the vessel herself, for she bore down with all the evidence of being skilfully handled, the anchor a–cockbill, the jib–boom guys already eased off, and standing by the side of the pilot, who was steering the Pharaon towards the narrow entrance of the inner port, was a young man, who, with activity and vigilant eye, watched every motion of the ship, and repeated each direction of the pilot.''',
                    '''Kalak rounded a rocky stone ridge and stumbled to a stop before the body of a dying thunderclast. The enormous stone beast lay on its side, riblike protrusions from its chest broken and cracked. The monstrosity was vaguely skeletal in shape, with unnaturally long limbs that sprouted from granite shoulders. The eyes were deep red spots on the arrowhead face, as if created by a fire burning deep within the stone. They faded. Even after all these centuries, seeing a thunderclast up close made Kalak shiver. The beast’s hand was as long as a man was tall. He’d been killed by hands like those before, and it hadn’t been pleasant. Of course, dying rarely was.''',
                    '''In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available. It is also used to temporarily replace text in a process called greeking, which allows designers to consider the form of a webpage or publication, without the meaning of the text influencing the design. Lorem ipsum is typically a corrupted version of De finibus bonorum et malorum, a 1st-century BC text by the Roman statesman and philosopher Cicero, with words altered, added, and removed to make it nonsensical and improper Latin. Versions of the Lorem ipsum text have been used in typesetting at least since the 1960s, when it was popularized by advertisements for Letraset transfer sheets.[1] Lorem ipsum was introduced to the digital world in the mid-1980s, when Aldus employed it in graphic and word-processing templates for its desktop publishing program PageMaker. Other popular word processors, including Pages and Microsoft Word, have since adopted Lorem ipsum,[2] as have many LaTeX packages,[3][4][5] web content managers such as Joomla! and WordPress, and CSS libraries such as Semantic UI.[6]''']

sample_text = choice(sample_text_list)


def check_words():
    start_button.config(bg='gray')
    time.sleep(60)
    box.config(state=DISABLED)
    words = box.get('1.0', 'end-1c')
    num_words = words.split(' ')
    num_words.remove(num_words[-1])
    sample_split = sample_text.split(' ')
    num_errors = 0
    for word in num_words:
        index = num_words.index(word)
        if word != sample_split[index]:
            num_errors += 1

    num_words_label = Label(text=f'You typed {len(num_words)} words!\nYou made {num_errors} error(s)')
    num_words_label.config(pady=10)
    num_words_label.grid(column=1, row=2)
    reset_button = Button(text='Reset', command=reset)
    reset_button.grid(column=1, row=3)


def reset():
    box.config(state=NORMAL)
    box.delete('1.0', 'end')
    start_button.config(bg='#f0f0f0')
    box.config(state=DISABLED)
    sample_label.destroy()
    new_text = choice(sample_text_list)
    new_label = Label(text=new_text, width=70, height=30, wraplength=350, justify='left')
    new_label.grid(column=0, row=0)


def new_thread():
    box.config(state=NORMAL)
    thread = Thread(target=check_words)
    thread.start()


sample_label = Label(text=sample_text, width=70, height=30, wraplength=350, justify='left')
sample_label.grid(column=0, row=0)

box = Text(height=20, width=75, wrap=WORD, state=DISABLED)
box.grid(column=1, row=0)

start_button = Button(text='Start', command=new_thread)
start_button.config(width=20)
start_button.grid(row=1, column=1)

window.mainloop()
