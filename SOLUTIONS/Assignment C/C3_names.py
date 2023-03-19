
class C3_names:

    def solution(self):
        """
        Method to create freq structure.
        """
        # initialize self.name to access values of names
        #intialize self.name_lengths to access the length on every value in names

        names = self.names
        count = {n : len(n) for n in names} 
        self.name_lengths = [i for i in count.values()]
        
        name_sort = sorted(list(set(count.values()))) #in ascending order sorting the length 
        f = {}
        for name_length in name_sort:
            f[name_length] = [i for i in names if len(i) == name_length] #calculate the length of the names

        freq_list = [(len(names), name_length, names) for name_length, names in f.items()] #order by number of name, name length, names

        freq_list.sort(key=lambda tup: tup[0]) #in ascending order sorting the result of freq_list 


        self.freq = {
            'most_freq': freq_list[-3:][::-1], 
            'least_freq': freq_list[:3]
        }
        return self


    def avg_name_length(self) -> float:
        """
        Return average name length.
        """

        if len(self.names): 
            return round((sum(self.name_lengths)/len(self.names)), 2)
        else:
            return 0


    def print_names_and_name_lengths(self, enabled=True): 
        """
        Print lists of names and name lengths.
        """
        if enabled:
            sep = '' if len(self.names) < 20 else '\n'
            print('\n')
            print(f'Names: {self.names}{sep}') #to print all the names in names
            print(f'Name lengths: {self.name_lengths}{sep}') #to print lenght of every name in names
        return self


    def print_freq(self, enabled=True):
        """
        Pretty-print freq struct.
        """
        if enabled:
            def limit(l_, n_):
                return str(l_) if len(l_) <= n_ else str(l_[0:n_]) + " ..."

            if self.freq != None:
                print('The three most frequent name lenghts are:')
                for m in self.freq['most_freq']:
                    print(f' - {m[0]:2} names of length {m[1]}: {limit(m[2], 5)}')
                print('\n')
                print('The three least frequent name lenghts are:')
                for m in self.freq['least_freq']:
                    print(f' - {m[0]:2} names of length {m[1]}: {limit(m[2], 5)}')
                #
            else:
                print('self.freq: not implemented in solution() method')
        #
        return self


    def print_avg_name_length(self, enabled=True): 
        """
        Print average name length.
        """
        if enabled:
            print(f'The average name length: {self.avg_name_length():.2f}')
        return self


    def __init__(self, names=['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller',
        'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White',
        'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark',
        'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez',
        'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Cox', 'Gomez',
        'Murray', 'Freeman', 'Wells', 'Webb', 'Simpson', 'Stevens', 'Tucker', 'Porter',
        'Hunter', 'Hicks', 'Crawford', 'Henry', 'Boyd', 'Mason', 'Morales', 'Kennedy',
        'Warren', 'Dixon', 'Ramos', 'Reyes', 'Burns', 'Gordon', 'Shaw', 'Holmes', 'Rice',
        'Robertson', 'Henderson', 'Patterson', 'Red', 'Willoughby', 'Fitzgerald']):
        """
        Constructor.
        """
        if names != None and type(names==list):
            self.names = names
        self.solution()


if __name__ == '__main__':
    """
    Main driver that starts program when called from command line.
    """
    #
    n1 = C3_names()   # use default list in C2_numbers
    n1.print_names_and_name_lengths() \
        .print_freq() \
        .print_avg_name_length()     # method chaining
    #
    n2 = C3_names(['Hans', 'Gretchen', 'Lotte', 'Gudrun', 'Ingrid'])   # use constructor list
    n2.print_names_and_name_lengths() \
         .print_freq() \
         .print_avg_name_length()     # method chaining