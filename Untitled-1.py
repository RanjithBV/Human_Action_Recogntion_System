class FIFOPageReplacement:
    def _init_(self, capacity):
        self.capacity = capacity  # Maximum number of frames in memory
        self.frames = []         # List to store the frames in memory
        self.page_set = set()    # Set to keep track of pages in memory

    def is_full(self):
        return len(self.frames) == self.capacity

    def replace_page(self, page):
        if self.is_full():
            # If memory is full, remove the first page (FIFO)
            removed_page = self.frames.pop(0)
            self.page_set.remove(removed_page)

        # Add the new page to memory
        self.frames.append(page)
        self.page_set.add(page)

    def access_page(self, page):
        if page not in self.page_set:
            self.replace_page(page)

    def display_memory(self):
        print("Current Page Frames:",self.frames)
        
if __name__ == "_main_":
    capacity = 3  # Set the capacity of memory frames
    fifo = FIFOPageReplacement(capacity)

    pages = [2, 3, 2, 1, 5, 2, 4, 5]

    for page in pages:
        fifo.access_page(page)
        fifo.display_memory()