class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        digits_list = []
        letters_list = []
        for log in logs: 
            if log.split()[1].isdigit():
                digits_list.append(log)
            else:
                letters_list.append(log)
        # letters_list.sort(key=lambda x: x.split()[0])
        # letters_list.sort(key=lambda x: x.split()[1:])
        letters_list.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters_list + digits_list

        