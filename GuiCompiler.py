from configparser import ConfigParser
import os
import tkinter as tk

ini_file = "FakeTest.ini"

# Idea search for test points with ocr
class GuiCompiler(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self)
        # TODO configparser loads data

        frames = self.load_ini(ini_file)
        # TODO create pages
        pages = self.create_frames(frames)

        # TODO init stuff that doesn't change (i.e. next bar)
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        self.page_frame = []

        for idx, page in enumerate(pages):
            self.page_frame.append(0)
            self.page_frame[idx] = page
            self.page_frame[idx].place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # todo
        self.curr = 0

        b_prev = tk.Button(buttonframe, text="PREV", command=lambda: self.page_frame[self.page_lifter(-1)].show())
        b_next = tk.Button(buttonframe, text="NEXT", command=lambda: self.page_frame[self.page_lifter(1)].show())

        b_prev.pack(side="left")
        b_next.pack(side="right")

        # Start at the first
        self.page_frame[self.page_lifter(self.curr)].show()
    #     self.update_vars()
    #
    # def update_vars(self):
    #     self.after(1000, self.update_vars())
    #     self.update()



    def load_ini(self, file):
        """
        frame attribute
        0: frame title
        1: instruction text
        2: upper_bound
        3: lower_bound if no lower_bound its the same as upper_bound
        4: picture file location - is not neccessary
        :param file: location of the ini_file
        :return: frame 2d array with multiple
        """
        config = ConfigParser()
        # TODO add check if file location exist
        config.read(file)

        num_of_frames = config.getint('init', 'num_of_pages')

        frames = []
        # todo what if attribute is not there
        for i in range(num_of_frames):
            frame_att = []
            frame_att.append(config.get('section_{}'.format(i), 'title_txt'))
            frame_att.append(config.get('section_{}'.format(i), 'instr_txt'))
            frame_att.append(config.getint('section_{}'.format(i), 'upper_bound'))
            frame_att.append(config.getint('section_{}'.format(i), 'lower_bound'))
            frames.append(frame_att)

        return frames

    def create_frames(self, frames):
        # todo
        pages = []
        for frame in frames:
            pages.append(PageCreator(frame))
        return pages

    def page_lifter(self, delta):
        # Todo Create button lifter
        if 0 <= self.curr + delta < len(self.page_frame):
            self.curr += delta
        print(self.curr)
        return self.curr




class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class PageCreator(Page):
    def __init__(self, frame_att, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text=frame_att[0])
        label.pack(side="top", fill="both", expand=True)

    def show(self):
        print("Pagecreator")
        self.tkraise()



if __name__ == "__main__":
    ini_file = "FakeTest.ini"
    root = tk.Tk()
    main = GuiCompiler(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()