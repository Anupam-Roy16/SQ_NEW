import re
from geopy.geocoders import Nominatim

class Qoute_validation:
    def __init__(self, qoute):
        self.qoute = qoute
        self.sanskrit_to_normal_char_map = {
            'ã': 'a', 'ñ': 'n', 'õ': 'o', 'ā': 'a', 'ć': 'c', 'ē': 'e',
            'ĩ': 'i', 'ī': 'i', 'ō': 'o', 'ś': 's', 'ũ': 'u', '।': '।',
            '॥': '॥', '़': 'o', 'ū': 'u', 'ḍ': 'd', 'ḏ': 'd', 'ḥ': 'h',
            'ḷ': 'l', 'ḹ': 'l', 'ḻ': 'l', 'ḿ': 'm', 'ṁ': 'm', 'ṃ': 'm',
            'ṅ': 'n', 'ṇ': 'n', 'ṉ': 'n', 'ṙ': 'r', 'ṛ': 'r', 'ṝ': 'r',
            'ṣ': 's', 'ṥ': 's', 'ṭ': 't', 'ẖ': 'h', 'ẽ': 'e'
        }
        self.is_valid = self.check_validity()


    def check_validity(self):
        try:
            self.title,self.body,self.reference,self.name,self.date,self.place,self.extra = self.qoute_parsing()
            
            if self.body_and_name_validity_check(self.body):
                var1 = True
            else:
                var1 = False
            if self.date_validity_check(self.date):
                var2 = True
            else:
                var2 = False
            if self.title_validity_check(self.title):
                var3 = True
            else:
                var3 = False
            if self.place_validity_check(self.place):
                var4 = True
               
            else:
                var4 = False
              
            if var1 and var2 and var3 and var4:
               
                return True
            else:
                if var1 == False:
                    print("body and name not valid")
                if var2 == False:
                    print("date not valid")
                if var3 == False:
                    print("title not valid")
                if var4 == False:
                    print("place not valid")
                return False
        except Exception as e:
            print(f"An error occurred during validation: {e}")
            return False



    def to_normal_text(self,text):
        return ''.join(self.sanskrit_to_normal_char_map.get(char, char) for char in text)

    def body_and_name_validity_check(self,body_text):
        body_words = re.findall(r'\b\S+\b', body_text)
        min_num_of_words = 10
        max_num_of_words = 1000
        if (len(body_words) >= min_num_of_words and len(body_words) <= max_num_of_words):
            return True
        else:
            return False

    def date_validity_check(self,input_date):
        # Define multiple patterns for different date formats
        patterns = [
                    r'\b\d{1,2}/\d{1,2}/\d{4}\b',  # MM/DD/YYYY or DD/MM/YYYY
                    r'\b\d{1,2}-\d{1,2}-\d{4}\b',  # MM-DD-YYYY or DD-MM-YYYY
                    r'\b\d{4}/\d{1,2}/\d{1,2}\b',  # YYYY/MM/DD
                    r'\b\d{4}-\d{1,2}-\d{1,2}\b',  # YYYY-MM-DD
                    r'\b\d{1,2}\.\d{1,2}\.\d{4}\b',  # DD.MM.YYYY or MM.DD.YYYY
                    r'\b\d{1,2}\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}\b',  # DD Month YYYY
                    r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}\b',  # Month DD, YYYY
                    r'\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}\b',  # DD Abbrev. Month YYYY
                    r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2},\s\d{4}\b',  # Abbrev. Month DD, YYYY
                    r'\b\d{8}\b',  # YYYYMMDD
                    r'\b\d{1,2}\s(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s\d{4}\b',  # DD Abbrev. Month YYYY (lowercase)
                    r'\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s\d{1,2},\s\d{4}\b',  # Abbrev. Month DD, YYYY (lowercase)
                    r'\b\d{4}\.\d{1,2}\.\d{1,2}\b',  # YYYY.MM.DD
                    r'\b\d{1,2}\s\w+\s\d{4}\b',  # DD Month YYYY (handles any word as month)
                    r'\b\w+\s\d{1,2},\s\d{4}\b',  # Month DD, YYYY (handles any word as month)
                    r'\b\d{1,2}-\w+-\d{4}\b',  # DD-Month-YYYY (handles any word as month)
                    r'\b\w+-\d{1,2}-\d{4}\b',  # Month-DD-YYYY (handles any word as month)
                    r'\b\d{1,2}/\d{1,2}/\d{2}\b',  # MM/DD/YY or DD/MM/YY
                    r'\b\d{1,2}-\d{1,2}-\d{2}\b',  # MM-DD-YY or DD-MM-YY
                    r'\b\d{2}\.\d{1,2}\.\d{1,2}\b',  # YY.MM.DD or DD.MM.YY
                    r'\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{2}\b',  # DD Abbrev. Month YY
                    r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2},\s\d{2}\b',  # Abbrev. Month DD, YY
                    r'\b\d{1,2}\s(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s\d{2}\b',  # DD Abbrev. Month YY (lowercase)
                    r'\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s\d{1,2},\s\d{2}\b',  # Abbrev. Month DD, YY (lowercase)
                    r'\b\d{4}\s\d{1,2}\s\d{1,2}\b',  # YYYY MM DD
                    r'\b\d{1,2}\s\d{1,2}\s\d{4}\b',  # DD MM YYYY
                    r'\b\d{1,2}\s\d{1,2}\s\d{2}\b',  # DD MM YY
                    r'\b\d{2}\s\d{1,2}\s\d{1,2}\b',  # YY MM DD
                    r'\b\d{1,2}\s(?:January|February|March|April|May|June|July|August|September|October|November|December),\s?\d{4}\b',
                    r'\b\d{1,2}\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s,\s?\d{4}\b',
                    
        ]

        # Find and print matches
        for pattern in patterns:
            matches = re.findall(pattern, input_date)
            if matches:
                return True
        return False


    def title_validity_check(self,input_string):
        pattern = r'^SQ\s*\d+$'
        if re.search(pattern, input_string):
            return True
        else:
            return False
    # Function to validate a location
    def place_validity_check(self,location_name):
        #since geolocator module can not detect sri dham maypur
        #it is solved by this way
        pattern = r"sri\s*dham\s*mayapur"
        match = re.search(pattern, location_name.lower())
        if match:
            return True
        
        geolocator = Nominatim(user_agent="location_validator",timeout=10)
        location = geolocator.geocode(location_name)
        if location:
            return True
        else:
            return False

    def qoute_parsing(self):
        qoute = self.qoute.strip()

        #title parsing.starting title is considerable. 
        pattern = r'^SQ\s*\d+'
        title_last_pos = -1
        title = ""
        match = re.search(pattern,qoute)
        if match:
            title_last_pos = match.end()
            title = match[0]
        else:
            print("title not found at start position")

        #body parsing. last reference starting with >>> Ref. is considered.
        pattern0 = r'>>> Ref.'
        ref_last_pos = -1
        ref_first_pos = -1
        matches = re.findall(pattern0,s)        
        if len(matches) ==0:
            print("No reference found")
        else:
           ref_first_pos = self.qoute.rfind(pattern0)
           ref_last_pos = ref_first_pos + len(pattern0)
          
        body = self.qoute[title_last_pos:ref_first_pos]

        # #immidiate date  after reference is parsed . date before reference is considered
        patterns = [
                    r'\b\d{1,2}/\d{1,2}/\d{4}\b',  # MM/DD/YYYY or DD/MM/YYYY
                    r'\b\d{1,2}-\d{1,2}-\d{4}\b',  # MM-DD-YYYY or DD-MM-YYYY
                    r'\b\d{4}/\d{1,2}/\d{1,2}\b',  # YYYY/MM/DD
                    r'\b\d{4}-\d{1,2}-\d{1,2}\b',  # YYYY-MM-DD
                    r'\b\d{1,2}\.\d{1,2}\.\d{4}\b',  # DD.MM.YYYY or MM.DD.YYYY
                    r'\b\d{1,2}\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}\b',  # DD Month YYYY
                    r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}\b',  # Month DD, YYYY
                    r'\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}\b',  # DD Abbrev. Month YYYY
                    r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2},\s\d{4}\b',  # Abbrev. Month DD, YYYY
                    r'\b\d{8}\b',  # YYYYMMDD
                    r'\b\d{1,2}\s(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s\d{4}\b',  # DD Abbrev. Month YYYY (lowercase)
                    r'\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s\d{1,2},\s\d{4}\b',  # Abbrev. Month DD, YYYY (lowercase)
                    r'\b\d{4}\.\d{1,2}\.\d{1,2}\b',  # YYYY.MM.DD
                    r'\b\d{1,2}\s\w+\s\d{4}\b',  # DD Month YYYY (handles any word as month)
                    r'\b\w+\s\d{1,2},\s\d{4}\b',  # Month DD, YYYY (handles any word as month)
                    r'\b\d{1,2}-\w+-\d{4}\b',  # DD-Month-YYYY (handles any word as month)
                    r'\b\w+-\d{1,2}-\d{4}\b',  # Month-DD-YYYY (handles any word as month)
                    r'\b\d{1,2}/\d{1,2}/\d{2}\b',  # MM/DD/YY or DD/MM/YY
                    r'\b\d{1,2}-\d{1,2}-\d{2}\b',  # MM-DD-YY or DD-MM-YY
                    r'\b\d{2}\.\d{1,2}\.\d{1,2}\b',  # YY.MM.DD or DD.MM.YY
                    r'\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{2}\b',  # DD Abbrev. Month YY
                    r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2},\s\d{2}\b',  # Abbrev. Month DD, YY
                    r'\b\d{1,2}\s(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s\d{2}\b',  # DD Abbrev. Month YY (lowercase)
                    r'\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s\d{1,2},\s\d{2}\b',  # Abbrev. Month DD, YY (lowercase)
                    r'\b\d{4}\s\d{1,2}\s\d{1,2}\b',  # YYYY MM DD
                    r'\b\d{1,2}\s\d{1,2}\s\d{4}\b',  # DD MM YYYY
                    r'\b\d{1,2}\s\d{1,2}\s\d{2}\b',  # DD MM YY
                    r'\b\d{2}\s\d{1,2}\s\d{1,2}\b',  # YY MM DD
                    r'\b\d{1,2}\s(?:January|February|March|April|May|June|July|August|September|October|November|December),\s?\d{4}\b',
                     r'\b\d{1,2}\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s,\s?\d{4}\b',
                    ]

        date_first_pos ,date_last_pos, date =  0,0,""
        dates =[]
        #print(self.qoute[ref_last_pos:])
        for pattern in patterns:
            dates += re.findall(pattern,self.qoute[ref_last_pos:])
        if len(dates) ==0:
            print("date not found after reference")
        else:
            date = dates[0]
            match = re.search(date, self.qoute[ref_last_pos:])
            date_first_pos = match.start() +ref_last_pos
            date_last_pos = match.end()+ ref_last_pos

        


        #since name is in first position is fixed
        #so by counting the number of words between name and date
        #we determine the place position
        temp  = self.qoute[ref_last_pos:date_first_pos]
        if re.search("aj ",temp):
            name_last_pos = re.search("aj ",temp).end()
        elif re.search("ja ",temp):
            name_last_pos = re.search("ja ",temp).end()
        elif re.search("mi ",temp):
            name_last_pos = re.search("mi ",temp).end()
        elif re.search("aka ",temp):
            name_last_pos = re.search("aka ",temp).end()
        elif re.search("āj ",temp):
            name_last_pos = re.search("āj ",temp).end()
        else:
            print("name not found error")

        words_between_name_and_date = re.findall(r'\b\S+\b', temp[name_last_pos:])

        if len(words_between_name_and_date) > 2:
            #place is in middle of name and date

            ref =self.qoute[ref_first_pos:date_last_pos]

            #find the name and starting postion of place
            tmp = 0
            name_last_pos = -1
            if re.search("Place :",temp):
                name_last_pos = re.search("Place :",temp).start()
                tmp = len("Place :")
            elif re.search("Place:",temp):
                name_last_pos = re.search("Place:",temp).start()
                tmp = len("Place:")
            elif re.search("place:",temp):
                name_last_pos = re.search("place:",temp).start()
                tmp = len("place:")
            elif re.search("place :",temp):
                name_last_pos = re.search("place :",temp).start()
                tmp = len("place :")
                #print("4")
            elif re.search(r"\bin\b",temp):
                f = re.search(r"\bin\b",temp)
                name_last_pos = f.start()
                matched_text = f.group()
            
                tmp = len(matched_text)
            elif re.search("ja ",temp):
                name_last_pos = re.search("ja ",temp).end()
           
            elif re.search("aj ",temp):
                name_last_pos = re.search("aj ",temp).end()
            elif re.search("āj ",temp):
                name_last_pos = re.search("āj ",temp).end()
            elif re.search("mi ",temp):
                name_last_pos = re.search("mi ",temp).end()
            elif re.search("aka ",temp):
                name_last_pos = re.search("aka ",temp).end()
         
            name = temp[:name_last_pos].strip()

            temp = temp[name_last_pos+tmp:].strip()

            #eliminate comma between name and place
            for i in range(len(temp)):
                    if temp[i] == " ":
                        pass
                    elif temp[i] != ",":
                        break
                    elif temp[i] == ",":
                        temp = temp[i+1:]
                        break

            #eliminate  "date:"" or  comma between place and date 
            match1 = re.search("Date :",temp)
            match2 = re.search("Date:",temp)
            match3 = re.search("date:",temp)
            match4 = re.search("date :",temp)
            match5 = re.search(r"\bon\b",temp)
            place = temp
            if match1:
                place = temp[:match1.start()]
            elif match2:
                place = temp[:match2.start()]
            elif match3:
                place = temp[:match3.start()]
            elif match4:
                place = temp[:match4.start()]
            elif match5:
                place = temp[:match5.start()]
            else:
                for i in range(len(place)-1,-1,-1):
                  
                    if place[i] == " ":
                        pass
                    elif place[i] != ",":
                        break
                    elif place[i] == ",":
                        place = place[:i]
                        break
            extra = qoute[date_last_pos:]
            if len(extra) > 20:
                print("invalid for extra words: ",extra)

        else:
            #place is after date

            #eliminate "date:" or  comma between name and date"
            name = temp
            match1 = re.search("Date :",name)
            match2 = re.search("Date:",name)
            match3 = re.search("date:",name)
            match4 = re.search("date :",name)
            match5 = re.search(r"\bon\b",temp)
            name1 = name
            if match1:
                name1 = name[:match1.start()]
            
            elif match2:
                name1 = name[:match2.start()]
            
            elif match3:
                name1 = name[:match3.start()]
            
            elif match4:
                name1 = name[:match4.start()]
            elif match5:
                name1 = name[:match5.start()]
            else:
                for i in range(len(name1)-1,-1,-1):
                    if name1[i] == " " or name1[i] == "\n":
                        pass
                    elif name1[i] != ",":
                        break
                    elif name1[i] == ",":
                        name1 = name1[:i]
                        break
            name = name1.strip()

            #check place exist or not
            place = self.qoute[date_last_pos:]
            words = re.findall(r'\b\S+\b', place)
            if len(words) == 0:
                print("no words in place")
            
            #eliminate "place:" or in or comma between date and place
            r = date_last_pos
            match1 = re.search("Place :",place)
            match2 = re.search("Place:",place)
            match3 = re.search("place:",place)
            match4 = re.search("place :",place)
            place1 = place
            if match1:
                place1 = place[match1.end():]
                r+=match1.end()
            elif match2:
                place1 = place[match2.end():]
                r+=match2.end()
            elif match3:
                place1 = place[match3.end():]
                r+=match3.end()
            elif match4:
                place1 = place[match4.end():]
                r+=match4.end()
            else:
                place_word = re.findall(r'\b\S+\b', place)
                if place_word[0] == "in":
                     match = re.search("in",place)
                     place1 = place[match.end():]
                     r+=match.end()
                else:
                    for i in range(len(place1)):
                        if place1[i] == " " or place1[i]=="\n":
                            pass
                        elif place1[i] != ",":
                            break
                        elif place1[i] == ",":
                            place1 = place1[i+1:]
                            r+=(i+1)
                            break

            place1 = place1.strip()
            temp_place = place1
            place1 = place1.split("\n")
            if len(place1) == 1:
                place_last_pos = place1[0].find(".")
                if place_last_pos == -1:
                    place_last_pos = len(place1[0])
                    extra = ""
                else:
                    extra = place1[0][place_last_pos+1:]
                place = place1[0][:place_last_pos]    
            else:
                place_last_pos = temp_place.find(".")
                if place_last_pos == -1:
                    place_last_pos = len(temp_place)
                    extra = ""
                else:
                    extra = temp_place[place_last_pos+1:]
                place = temp_place[:place_last_pos]

            if len(extra)>20:
                print("invalid for extra words",extra)
            place_last_pos = (len(place)+ self.qoute.rfind(place))
            ref =self.qoute[ref_first_pos:place_last_pos]
            
        return title,body,ref,name,date,place,extra



s ="""SQ 123 
we want  the   shelter of Lord 2 Jan 2078 Caitanya’s lotus >>> Ref. feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapataka Swami
Date: 24 December, 2022
Place: Sridham Mayapur."""
s1="""SQ 123 
we want  the   shelter of Lord 2 Jan 2078 Caitanya’s lotus >>> Ref. feet,and thus we can taste the nectar all the time.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja 28 Jun 2023
place: Śrī Māyāpur, India . Hare Krishna Hare Krishna Krishna Krishna
 Hare Hare Hare Ram Hare Ram Ram Ram Hare Hare . Iskon dhaka
"""





ob = Qoute_validation(s)
print(ob.is_valid)
if ob.is_valid:

    print("Title","\n","------","\n",ob.title,"\n")
    print("body","\n","------","\n",ob.body,"\n")
    print("reference","\n","------","\n",ob.reference,"\n")
    print("Name","\n","------","\n",ob.name,"\n")
    print("date","\n","------","\n",ob.date,"\n")
    print("place","\n","------","\n",ob.place,"\n")
    print("extra","\n","------","\n",ob.extra,"\n")

