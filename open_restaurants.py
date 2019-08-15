def level1():
    import pandas, re

    #get the file
    df = pandas.read_csv("restaurant_hours.csv", header=None)
    df.columns = ["restaurant", "hours"]

    #Make list of hotel names and list of opening days/time
    open1 = [item for item in df.hours]
    open1 = [line.lower() for line in open1]
    rest = [item.lower() for item in df.restaurant]

    #############
    ##Level2
    ''' Import data for use and put in desired type: list, for use '''
    ###############
    #Transorm data to get desired formats for each open day(s) and corresponding time
    #Use regex to find the first two matching numbers to be time for each split at '/'
    import pandas, re, datetime

    df = pandas.read_csv("restaurant_hours.csv", header=None)
    df.columns = ["restaurant", "hours"]
    #df.head()

    #Make list of hotel names and list of opening days/time
    open1 = [item for item in df.hours]
    open1 = [line.lower() for line in open1]
    rest = [item.lower() for item in df.restaurant]

    daysOpen = []
    openTimes = []
    fullmeasure = []

    #my seperators
    sep = "|"
    sep2 = " "
    sep3 = "--"
    comma = ","
    for line, res,  in zip(open1, rest):
        line = line.replace(':', '')
        parts = "(\d+)"
        #Start trying for splits of day and time
        if len(line.split('/')) == 1:
            x = line.split('/')[0].split() #first split group: first listed day(s)
            startx = ''.join(re.findall(parts, str(x))[0]) #find and grab matching time slots for opening time
            startx_pOd = ''.join(re.findall("am|pm", str(x))[0]) #Find and grab pOd = Period of day: am or pm for open time
            closex = ''.join(re.findall(parts, str(x))[1]) #find and grab matching time slots for closing time
            closex_pOd = ''.join(re.findall("am|pm", str(x))[1]) # grab pOd for close
            dayx = x[0] #take first item as the first listed day(s).
            try:
                dayx2 = int(x[1]) #trying to see if this is a second listed day or a time. Forget if a time
            except:
                dayx2 = x[1] #It's not a time as int() fails so pick it as 2nd listed day
            if type(dayx2) != int: #means the exception occurred, it's a day! Picking it...
                daysOpen.append(dayx + sep + dayx2)
                openTimes.append(res + sep + startx + sep2 + startx_pOd + sep2 + sep3 + closex + sep2 + closex_pOd + sep + startx + sep2 + startx_pOd + sep2 + sep3 + closex + sep2 + closex_pOd)
            else: #if it's not a day slot (int() worked), just take the first one only.
                daysOpen.append(dayx)
                openTimes.append(res + sep + startx + sep2 + startx_pOd + sep2 + sep3 + closex + sep2 + closex_pOd)

        #For the entries with two groups of open day/time
        elif len(line.split('/')) == 2:
            a = line.split('/')[0].split() #first split group: first listed day(s)
            b = line.split('/')[1].split() #2nd split group
            starta = ''.join(re.findall(parts, str(a))[0])
            starta_pOd = ''.join(re.findall("am|pm", str(a))[0]) #Find and grab pOd for open time1
            closea = ''.join(re.findall(parts, str(a))[1])
            closea_pOd = ''.join(re.findall("am|pm", str(a))[1]) # Find and grab pOd for close time1
            startb = ''.join(re.findall(parts, str(b))[0])
            startb_pOd = ''.join(re.findall("am|pm", str(b))[0]) #Find and grab pOd for open time2
            closeb = ''.join(re.findall(parts, str(b))[1])
            closeb_pOd = ''.join(re.findall("am|pm", str(b))[1]) # grab pOd for close time 2
            daya = a[0]
            dayb = b[0]
            try:
                daya2 = int(x[1]) #trying to see if this a second listed day or a time. Forget if a time
            except:
                daya2 = x[1] #It's not a time as int() fails so pick it as 2nd listed day
            #######
            # PS, no need to look for a second day entry since none has it that way from eyeballing the result
            #######
            if type(daya2) != int:
                daysOpen.append(daya + sep + daya2 + sep + dayb)
                print("{} is also open on {} \n\n".format(res, daya2))
            else:
                daysOpen.append(daya + sep + dayb)
            openTimes.append(res + sep + starta + sep2 + starta_pOd + sep2 + sep3 + closea + sep2 + closea_pOd + sep + startb + sep2 + startb_pOd + sep2 + sep3 + closeb + sep2 + closeb_pOd)

        elif len(line.split('/')) == 3:
            c = line.split('/')[0].split() #first split group
            d = line.split('/')[1].split() #2nd split group
            startc = ''.join(re.findall(parts, str(c))[0]) #find and grab matching time slots for opening time1
            startc_pOd = ''.join(re.findall("am|pm", str(c))[0]) #Find and grab pOd for open time1
            closec = ''.join(re.findall(parts, str(c))[1]) #find and grab matching time slots for closing time1
            closec_pOd = ''.join(re.findall("am|pm", str(c))[1]) # Find and grab pOd for close time1
            startd = ''.join(re.findall(parts, str(d))[0]) #find and grab matching time slots for opening time2
            startd_pOd = ''.join(re.findall("am|pm", str(d))[0]) #Find and grab pOd for open time2
            closed = ''.join(re.findall(parts, str(d))[1]) #find and grab matching time slots for closing time2
            closed_pOd = ''.join(re.findall("am|pm", str(d))[1]) # grab pOd for close time 2
            dayc = c[0]
            dayd = d[0]
            try:
                dayc2 = int(x[1]) #trying to see if this a second listed day or a time. Forget if a time
            except:
                dayc2 = x[1] #It's not a time as int() fails so pick it as 2nd listed day
            #print(c, d)
            #print("{} is open {} to {} every {} AND {} to {} every {}\n".format(res, startc, closec, dayc, startd, closed, dayd))
            #######
            #PS, no need to look for a second day entry since none has it that way from eyeballing the result
            #######
            if type(dayc2) != int:
                daysOpen.append(dayc + sep + dayc2 + sep + dayd)
                print("{} is also open on {} \n\n".format(res, dayc2))
            else:
                daysOpen.append(dayc + sep + dayd)
            openTimes.append(res + sep + startc + sep2 + startc_pOd + sep2 + sep3 + closec + sep2 + closec_pOd + sep + startd + sep2 + startd_pOd + sep2 + sep3 + closed + sep2 + closed_pOd)

        elif len(line.split('/')) == 4:
            o = line.split('/')[0].split() #first split group
            p = line.split('/')[1].split() #2nd split group
            starto = ''.join(re.findall(parts, str(o))[0])
            starto_pOd = ''.join(re.findall("am|pm", str(o))[0]) #Find and grab pOd for open time1
            closeo = ''.join(re.findall(parts, str(o))[1])
            closeo_pOd = ''.join(re.findall("am|pm", str(o))[1]) # Find and grab pOd for close time1
            startp = ''.join(re.findall(parts, str(p))[0])
            startp_pOd = ''.join(re.findall("am|pm", str(p))[0]) #Find and grab pOd for open time2
            closep = ''.join(re.findall(parts, str(p))[1])
            closep_pOd = ''.join(re.findall("am|pm", str(p))[1]) # grab pOd for close time 2
            dayo = o[0]
            dayp = p[0]
            try:
                dayo2 = int(x[1]) #trying to see if this a second listed day or a time. Forget if a time
            except:
                dayo2 = x[1] #It's not a time as int() fails so pick it as 2nd listed day

            #PS, no need to look for a second day entry since none has it that way from eyeballing the result
            if type(dayo2) != int:
                daysOpen.append(dayo+ sep + dayo2 + sep + dayp)
                print("{} is also open on {} \n\n".format(res, dayo2))
            else:
                daysOpen.append(dayo + sep + dayp)
            openTimes.append(res + sep + starto + sep2 + starto_pOd + sep2 + sep3 + closeo + sep2 + closeo_pOd + sep + startp + sep2 + startp_pOd + sep2 + sep3 + closep + sep2 + closep_pOd)

    #Merger (removing the trailing comma) daysOpen with openTimes for a comprehensive list of days open and their open times
    for x, y in zip(openTimes, daysOpen):
        fullmeasure.append(x + sep + y.replace(',', ''))

    return fullmeasure

def level2(x):
    ##Level3b
    ''' Data Transformation 2
    Using the returned list from level1, remove sat and sun with their corresponding time slot
    '''
    sep = "|"
    sep2 = " "
    sep3 = "--"
    comma = ","
    fullmeasureUpdated = []
    for line in x:
        target = line.split('|')
        if len(target) == 5:
            x = target[-1]
            if (x.startswith('sat') and x.endswith('sun')) or x == 'sat' or x == 'sun': #if it's a match
                target.pop(4) #remove the day value
                target.pop(2) #pop open/close time(bearing in mind the shifted index)
            fullmeasureUpdated.append(sep.join(target)) #return the value seperated with our seperator
        elif len(target) == 3:
            fullmeasureUpdated.append(line)
    return fullmeasureUpdated

def level3(y):
    #############
    ##Level3c
    ''' Data Transformation 3
        Transform time slot to match the hour minute HH:MM format
        '''
    ###############
    sep = "|"
    sep2 = " "
    sep3 = "--"
    comma = ","
    converted = []
    for line in y:
        x = line.split('|')
        #################
        #For listings with only one day/time entry
        #################
        if len(x) == 3:
            o = x[1].split(' --')[0] #open time in "11 am" format
            c = x[1].split(' --')[1] #close time in "11 am" format
            opened = o.split()[0] #open time in "1" format
            closed = c.split()[0] #close time in "1" format
            open_tOd = o.split()[1] #am/pm of open time
            close_tOd = c.split()[1] #am/pm of close time

            ############
            # Opening Times
            ##############
            #For those with opening in am,convert accordingy
            if open_tOd == 'am':
                if len(opened) == 1:
                    openTime1 = '0' + opened + '00' #put a zero infront and two after
                elif len(opened) == 2:
                    openTime1 = opened + '00' #put 2 zeros after
                elif len(opened) == 3:
                    openTime1 = '0' + opened #put a zero before
                elif len(opened) == 4:
                    openTime1 = opened #return it. right format

            #For those with opening in pm,convert accordingy
            elif open_tOd == 'pm':
                if len(opened) == 1:
                    opened = int(opened)
                    opened += 12 #convert to 12hour format
                    openTime1 = str(opened) + '00' #put 2 zeros after  to complete format
                elif len(opened) == 2:
                    opened = int(opened)
                    if opened == 12:
                        openTime1 = str(opened) + '00'
                    elif opened < 12:
                        opened += 12
                        openTime1 = str(opened) + '00' #put 2 zeros after  to complete format
                elif len(opened) == 3:
                    openedi = opened #hold the string format for later use
                    opened = opened[0]
                    opened = int(opened)
                    opened += 12
                    openTime1 = str(opened) + openedi[1:] #add the last two to complete
                elif len(opened) == 4:
                    openedi = opened #hold the string format for later use
                    opened = opened[:2] #take the fisrt 2 numbers ie hours
                    opened = int(opened)
                    opened += 12
                    openTime1 = str(opened) +  openedi[2:] #add the last two to complete


            ############
            # Closing Times
            ##############
            #For those with closing in am,convert accordingy
            if close_tOd == 'am':
                if len(closed) == 1:
                    closeTime1 = '0' + closed + '00' #put a zero infront and two after
                elif len(closed) == 2:
                    closeTime1 = closed + '00' #put 2 zeros after
                elif len(closed) == 3:
                    closeTime1 = '0' + closed  #put a zero before
                elif len(closed) == 4:
                    closeTime1 = closed #return it. right format

            #For those with closing in pm,convert accordingy
            elif close_tOd == 'pm':
                if len(closed) == 1:
                    closed = int(closed)
                    closed += 12 #convert to 12hour format
                    closeTime1 = str(closed) + '00' #put 2 zeros after  to complete format
                elif len(closed) == 2:
                    closed = int(closed)
                    if closed == 12:
                        closeTime1 = str(closed) + '00'
                    elif closed < 12:
                        closed += 12
                        closeTime1 = str(closed) + '00' #put 2 zeros after  to complete format
                elif len(closed) == 3:
                    closedi = closed #hold the string format for later use
                    closed = closed[0]
                    closed = int(closed)
                    closed += 12
                    closeTime1 = str(closed) + closedi[1:] #add the last two to complete
                elif len(closed) == 4:
                    closedi = closed #hold the string format for later use
                    closed = closed[:2]
                    closed = int(closed)
                    closed += 12
                    closeTime1 = str(closed) +  closedi[2:] #add the last two to complete
            #Add to converted: restaurant name, open time, close time, days open with seperators
            converted.append(x[0] + sep + openTime1 + sep + closeTime1 + sep + x[2]) #Put it all together

        ################
        #For listings with two day/time entry
        ###################
        if len(x) == 5:
            o = x[1].split(' --')[0] #1st open time in "11 am" format
            o2 = x[2].split(' --')[0] #2nd open time in "11 am" format
            c = x[1].split(' --')[1] #1st close time in "11 am" format
            c2 = x[2].split(' --')[1] #2nd close time in "11 am" format
            opened = o.split()[0] #1st open time in "1" format
            opened2 = o2.split()[0] #2nd open time in "1" format
            closed = c.split()[0] #1st close time in "1" format
            closed2 = c2.split()[0] #2nd close time in "1" format
            open_tOd = o.split()[1] #1st am/pm of open time
            open_tOd2 = o2.split()[1] #2nd am/pm of open time
            close_tOd = c.split()[1] #1st am/pm of close time
            close_tOd2 = c2.split()[1] #1st am/pm of close time

            #First opening time
            #For those with opening in am,convert accordingy
            if open_tOd == 'am':
                if len(opened) == 1:
                    openTime1 = '0' + opened + '00' #put a zero infront and two after
                elif len(opened) == 2:
                    openTime1 = opened + '00' #put 2 zeros after
                elif len(opened) == 3:
                    openTime1 = '0' + opened #put a zero before
                elif len(opened) == 4:
                    openTime1 = opened #return it. right format


            #For those with opening in pm,convert accordingy
            elif open_tOd == 'pm':
                if len(opened) == 1:
                    opened = int(opened)
                    opened += 12 #convert to 12hour format
                    openTime1 = str(opened) + '00' #put 2 zeros after  to complete format
                elif len(opened) == 2:
                    opened = int(opened)
                    if opened == 12:
                        openTime1 = str(opened) + '00'
                    elif opened < 12:
                        opened += 12
                        openTime1 = str(opened) + '00' #put 2 zeros after  to complete format
                elif len(opened) == 3:
                    openedi = opened #hold the string format for later use
                    opened = opened[0]
                    opened = int(opened)
                    opened += 12
                    openTime1 = str(opened) + openedi[1:] #add the last two to complete
                elif len(opened) == 4:
                    openedi = opened #hold the string format for later use
                    opened = opened[:2]
                    opened = int(opened)
                    opened += 12
                    openTime1 = str(opened) +  openedi[2:] #add the last two to complete

            #Second opening time
            #For those with opening in am,convert accordingy
            if open_tOd2 == 'am':
                if len(opened2) == 1:
                    openTime2 = '0' + opened + '00' #put a zero infront and two after
                elif len(opened2) == 2:
                    openTime2 = opened2 + '00' #put 2 zeros after
                elif len(opened2) == 3:
                    openTime2 = '0' + opened2  #put a zero before
                elif len(opened2) == 4:
                    openTime2 = opened2 #return it. right format

            #For those with opening in pm,convert accordingy
            elif open_tOd2 == 'pm':
                if len(opened2) == 1:
                    opened2 = int(opened2)
                    opened2 += 12 #convert to 12hour format
                    openTime2 = str(opened2) + '00' #put 2 zeros after  to complete format
                elif len(opened2) == 2:
                    opened2 = int(opened2)
                    if opened2 == 12:
                        openTime2 = str(opened2) + '00'
                    elif opened2 < 12:
                        opened2 += 12
                        openTime2 = str(opened2) + '00' #put 2 zeros after  to complete format
                elif len(opened2) == 3:
                    openedi = opened2 #hold the string format for later use
                    opened2 = opened2[0]
                    opened2 = int(opened2)
                    opened2 += 12
                    openTime2 = str(opened2) + openedi[1:] #add the last two to complete
                elif len(opened2) == 4:
                    openedi = opened2 #hold the string format for later use
                    opened2 = opened2[:2] #extract the first 2 the hours
                    opened2 = int(opened2)
                    opened2 += 12
                    openTime2 = str(opened2) +  openedi[2:] #add the last two to complete

            ############
            # Closing Time 1
            ##############
            #For those with closing in am,convert accordingy
            if close_tOd == 'am':
                if len(closed) == 1:
                    closeTime1 = '0' + closed + '00' #put a zero infront and two after
                elif len(closed) == 2:
                    closeTime1 = closed + '00' #put 2 zeros after
                elif len(closed) == 3:
                    closeTime1 = '0' + closed #put a zero before
                elif len(closed) == 4:
                    closeTime1 = closed #return it. right format

            #For those with closing in pm,convert accordingy
            elif close_tOd == 'pm':
                if len(closed) == 1:
                    closed = int(closed)
                    closed += 12 #convert to 12hour format
                    closeTime1 = str(closed) + '00' #put 2 zeros after  to complete format
                elif len(closed) == 2:
                    closed = int(closed)
                    if closed == 12:
                        closeTime1 = str(closed) + '00'
                    elif closed < 12:
                        closed += 12
                        closeTime1 = str(closed) + '00' #put 2 zeros after  to complete format
                elif len(closed) == 3:
                    closedi = closed #hold the string format for later use
                    closed = closed[0]
                    closed = int(closed)
                    closed += 12
                    closeTime1 = str(closed) + closedi[1:] #add the last two to complete
                elif len(closed) == 4:
                    closedi = closed #hold the string format for later use
                    closed = closed[:2]
                    closed = int(closed)
                    closed += 12
                    closeTime1 = str(closed) +  closedi[2:] #add the last two to complete

            ############
            # Closing Time 2
            ##############
            #For those with closing in am,convert accordingy
            if close_tOd2 == 'am':
                if len(closed2) == 1:
                    closeTime2 = '0' + closed + '00' #put a zero infront and two after
                elif len(closed2) == 2:
                    closeTime2 = closed2 + '00' #put 2 zeros after
                elif len(closed2) == 3:
                    closeTime2 = '0' + closed2 #put a zero before
                elif len(closed2) == 4:
                    closeTime2 = closed2 #return it. right format

            #For those with closing in pm,convert accordingy
            elif close_tOd2 == 'pm':
                if len(closed2) == 1:
                    closed2 = int(closed2)
                    closed2 += 12 #convert to 12hour format
                    closeTime2 = str(closed2) + '00' #put 2 zeros after  to complete format
                elif len(closed2) == 2:
                    closed2 = int(closed2)
                    if closed2 == 12:
                        closeTime2 = str(closed2) + '00'
                    elif closed2 < 12:
                        closed2 += 12
                        closeTime2 = str(closed2) + '00' #put 2 zeros after  to complete format
                elif len(closed2) == 3:
                    closedi = closed2 #hold the string format for later use
                    closed2 = closed2[0] #extract the first figure ie hour
                    closed2 = int(closed2)
                    closed2 += 12
                    closeTime2 = str(closed2) + closedi[1:] #add the last two to complete
                elif len(closed2) == 4:
                    closedi = closed2 #hold the string format for later use
                    closed2 = closed2[:2]
                    closed2 = int(closed2)
                    closed2 += 12
                    closeTime2 = str(closed2) +  closedi[2:] #add the last two to complete
            converted.append(x[0] + sep + openTime1 + sep + closeTime1 + sep + openTime2 + sep + closeTime2 + sep + x[3] + sep + x[4]) #Put it all together
    return converted

def level4(z):
    '''
    #Level3d
    Data Transformation 4 Covnersion of day formats for update of dataset
    #Level3e
    Data Transformation 5: Update data set to have all day group slots match their respective open and close tags
    '''
    sep = "|"
    sep2 = " "
    sep3 = "--"
    comma = ","
    mon_sun = "--mon|tue|wed|thu|fri"
    mon_sat = "--mon|tue|wed|thu|fri"
    mon_fri = "--mon|tue|wed|thu|fri"
    mon_thu = "--mon|tue|wed|thu"
    mon_wed = "--mon|tue|wed"
    wed_sun = "--wed|thu|fri"
    fri_sat = "--fri"
    fri_sun = "--fri"
    thu_fri = "--thu|fri"
    mon = "--mon"
    tue = "--tue"
    wed = "--wed"
    thu = "--thu"
    fri = "--fri"

    def finder(x, y):
        if x[-1] == "mon-sun":
            x.pop(-1)
            x.insert(3, mon_sun)
        elif x[-1] == "mon-sat":
            x.pop(-1)
            x.insert(3, mon_sat)
        elif x[-1] == "mon-fri":
            x.pop(-1)
            x.insert(3, mon_fri)
        elif x[-1] == "mon-thu":
            x.pop(-1)
            x.insert(3, mon_thu)
        elif x[-1] == "mon-wed":
            x.pop(-1)
            x.insert(3, mon_wed)
        elif x[-1] == "wed-sun":
            x.pop(-1)
            x.insert(3, wed_sun)
        elif x[-1] == "fri-sat":
            x.pop(-1)
            x.insert(3, fri_sat)
        elif x[-1] == "fri-sun":
            x.pop(-1)
            x.insert(3, fri_sun)
        elif x[-1] == "thu-fri":
            x.pop(-1)
            x.insert(3, thu_fri)
        elif x[-1] == "mon":
            x.pop(-1)
            x.insert(3, mon)
        elif x[-1] == "tue":
            x.pop(-1)
            x.insert(3, tue)
        elif x[-1] == "wed":
            x.pop(-1)
            x.insert(3, wed)
        elif x[-1] == "thu":
            x.pop(-1)
            x.insert(3, thu)
        elif x[-1] == "fri":
            x.pop(-1)
            x.insert(3, fri)
        y.append(x[0] + sep3 + x[1] + sep + x[2] + x[3])

    def finder2(x, y):
        #first day slot change
        if x[-1] == "mon-sun":
            x.pop(-1)
            x.insert(6, mon_sun)
            #print(x)
        elif x[-1] == "mon-sat":
            x.pop(-1)
            x.insert(6, mon_sat)
        elif x[-1] == "mon-fri":
            x.pop(-1)
            x.insert(6, mon_fri)
        elif x[-1] == "mon-thu":
            x.pop(-1)
            x.insert(6, mon_thu)
        elif x[-1] == "mon-wed":
            x.pop(-1)
            x.insert(6, mon_wed)
        elif x[-1] == "wed-sun":
            x.pop(-1)
            x.insert(6, wed_sun)
        elif x[-1] == "fri-sat":
            x.pop(-1)
            x.insert(6, fri_sat)
        elif x[-1] == "fri-sun":
            x.pop(-1)
            x.insert(6, fri_sun)
        elif x[-1] == "thu-fri":
            x.pop(-1)
            x.insert(6, mon_sat)
        elif x[-1] == "mon":
            x.pop(-1)
            x.insert(6, mon)
        elif x[-1] == "tue":
            x.pop(-1)
            x.insert(6, tue)
        elif x[-1] == "wed":
            x.pop(-1)
            x.insert(3, wed)
        elif x[-1] == "thu":
            x.pop(-1)
            x.insert(6, thu)
        elif x[-1] == "fri":
            x.pop(-1)
            x.insert(6, fri)

        #Second day slot change
        if x[-2] == "mon-sun":
            x.pop(-2)
            x.insert(5, mon_sun)
        elif x[-2] == "mon-sat":
            x.pop(-2)
            x.insert(5, mon_sat)
        elif x[-2] == "mon-fri":
            x.pop(-2)
            x.insert(5, mon_fri)
        elif x[-2] == "mon-thu":
            x.pop(-2)
            x.insert(5, mon_thu)
        elif x[-2] == "mon-wed":
            x.pop(-2)
            x.insert(5, mon_wed)
        elif x[-2] == "wed-sun":
            x.pop(-2)
            x.insert(5, wed_sun)
        elif x[-2] == "fri-sat":
            x.pop(-2)
            x.insert(5, fri_sat)
        elif x[-2] == "fri-sun":
            x.pop(-2)
            x.insert(5, fri_sun)
        elif x[-2] == "thu-fri":
            x.pop(-2)
            x.insert(5, mon_sat)
        elif x[-2] == "mon":
            x.pop(-2)
            x.insert(5, mon)
        elif x[-2] == "tue":
            x.pop(-2)
            x.insert(5, tue)
        elif x[-2] == "wed":
            x.pop(-2)
            x.insert(3, wed)
        elif x[-2] == "thu":
            x.pop(-2)
            x.insert(5, thu)
        elif x[-2] == "fri":
            x.pop(-2)
            x.insert(5, fri)
        y.append(x[0] + sep3 + x[1] + sep + x[2] + sep3 + x[3] + sep + x[4] + sep + x[5] + sep + x[6])

    converted_dict = []
    for line in z:
        x = line.split('|')
        if len(x) == 4:
            finder(x, converted_dict)
        elif len(x) == 7:
            finder2(x, converted_dict)

    return converted_dict

def level5(x):
    '''
    #Level3e
    Data Transformation 6: Convert times to datetime.time()
    '''
    import datetime
    restaurants = []
    for line in x:
        rows = line.split('--')
        if len(rows) == 3:
            timer = rows[1]
            opener = timer.split('|')[0]
            closer = timer.split('|')[1]
            #Convert Opening Time
            if opener.startswith("0"):
                opener = opener[1:] #remove first item
                hour = opener[0] #take first item
                minute = opener[1:] #take remaining two item
                opener = datetime.time(int(hour), int(minute)) #make a datetime with 9,30
            elif opener == "2400":
                opener = datetime.time(0,0) #make a datetime with 9,30
            else:
                hour = opener[:2]
                minute = opener[2:]
                opener = datetime.time(int(hour), int(minute)) #make a datetime with 9,30

            #Convert Closing Time
            if closer.startswith("0"):
                closer = closer[1:] #remove first item
                hour = closer[0] #take first item
                minute = closer[1:] #take remaining two item
                closer = datetime.time(int(hour), int(minute)) #make a datetime with 9,30
            elif closer == "2400":
                closer = datetime.time(0,0) #make a datetime with 9,30
            else:
                hour = closer[:2]
                minute = closer[2:]
                closer = datetime.time(int(hour), int(minute)) #make a datetime with 9,30
            restaurants.append([rows[0], opener, closer, rows[-1]])

        #For the group of 2 open day and time
        elif len(rows) == 5:
            timer1 = rows[1]
            timer2 = rows[2]
            opener1 = timer1.split('|')[0]
            closer1 = timer1.split('|')[1]
            opener2 = timer2.split('|')[0]
            closer2 = timer2.split('|')[1]

            #Convert first Opening and Closing Time
            #Conveerting Opener1
            if opener1.startswith("0"):
                opener1 = opener1[1:] #remove first item
                hour = opener1[0] #take first item
                minute = opener1[1:] #take remaining two item
                opener1 = datetime.time(int(hour), int(minute)) #make a datetime with 9,30
            elif opener1 == "2400":
                opener1 = datetime.time(0,0) #make a datetime with 9,30
            else:
                hour = opener1[:2]
                minute = opener1[2:]
                opener1 = datetime.time(int(hour), int(minute)) #make a datetime with 9,30

            #Convert Closer1
            if closer1.startswith("0"):
                closer1 = closer1[1:] #remove first item
                hour = closer1[0] #take first item
                minute = closer1[1:] #take remaining two item
                closer1 = datetime.time(int(hour), int(minute)) #make a datetime with 9,30
            elif closer1 == "2400":
                closer1 = datetime.time(0,0) #make a datetime with 9,30
            else:
                hour = closer1[:2]
                minute = closer1[2:]
                closer1 = datetime.time(int(hour), int(minute)) #make a datetime with 9,30

            #Convert second Opening and Closing Time
            #Converting Opener2
            if opener2.startswith("0"):
                opener2 = opener2[1:] #remove first item
                hour = opener2[0] #take first item
                minute = opener2[1:] #take remaining two item
                opener2 = datetime.time(int(hour), int(minute)) #make a datetime with 9,30
            elif opener2 == "2400":
                opener2 = datetime.time(0,0) #make a datetime with 9,30
            else:
                hour = opener2[:2]
                minute = opener2[2:]
                opener2 = datetime.time(int(hour), int(minute)) #make a datetime with 9,30

            #Convert Closer2
            if closer2.startswith("0"):
                closer2 = closer2[1:] #remove first item
                hour = closer2[0] #take first item
                minute = closer2[1:] #take remaining two item
                closer2 = datetime.time(int(hour), int(minute)) #make a datetime with 9,30
            elif closer2 == "2400":
                closer2 = datetime.time(0,0) #make a datetime with 9,30
            else:
                hour = closer2[:2]
                minute = closer2[2:]
                closer2 = datetime.time(int(hour), int(minute)) #make a datetime with 9,30
            restaurants.append([rows[0], opener1, closer1, opener2, closer2, rows[-2], rows[-1]])

    return restaurants

def find_open_restaurants():
    import datetime
    fullmeasure = level1()
    fullmeasureUpdated = level2(fullmeasure)
    converted = level3(fullmeasureUpdated)
    converted_dict = level4(converted)
    restaurants= level5(converted_dict)


    print("Warm welcome to our restaurant finder service! What time are we looking at (HH:MM)")
    userTime = input(">>>")
    userTime = userTime.replace(':', '')
    try:
        hour = int(userTime[:2])
        minute = int(userTime[2:])
    except:
        print("We will need time as numbers")

    try:
        time = datetime.time(hour, minute)

        print("What day of the week please like 'mon' through 'fri':")
        userDay = input(">>>")

        ##Level4
        #The last part of the funtion to get open restaurants
        #Start an empty list of open restaurants for possible population
        open_rests = []

        ##Function begins
        for line in restaurants:
            restaurant = line[0] #name of restaurant

            #For single opening days group
            #Add to the list of ipen restaurants if userday and time match an open day and time
            if len(line) == 4:
                oTime1 = line[1] #opening time
                cTime1 = line[2] #closing time
                #print(time <= cTime1)
                days1 = line[3].split('|') #open days group
                #print(userDay in days1)
                if userDay == "sat":
                    pass
                elif userDay == "sun":
                    pass
                elif userDay in days1:
                    if time >= oTime1: #if listed user time or open time or after it
                        if time <= cTime1: #and if user time is before close time
                            oTime1 = oTime1.strftime("%H:%M")
                            cTime1 = cTime1.strftime("%H:%M")
                            open_rests.append("{} is open from {} to {}".format(restaurant, oTime1,cTime1))

            #For double opening days group
            #Add to the list of ipen restaurants if userday and time match an open day and time in two opener days
            #First group
            elif len(line) == 7:
                oTime1 = line[1] #opening time1
                cTime1 = line[2] #closing time1
                days1 = line[5] #open days group 1
                if userDay == "sat":
                    pass
                elif userDay == "sun":
                    pass
                elif userDay in days1:
                    if time >= oTime1: #if listed user time or open time or after it
                        if time < cTime1: #and if user time is before close time
                            oTime1 = oTime1.strftime("%H:%M")
                            cTime1 = cTime1.strftime("%H:%M")
                            open_rests.append("{} is open from {} to {}".format(restaurant, oTime1, cTime1))

                #Second group
                oTime2 = line[3] #opening time2
                cTime2 = line[4] #closing time2
                days2 = line[6] #open days group 2
                if userDay == "sat":
                    pass
                elif userDay == "sun":
                    pass
                elif userDay in days2:
                    if time >= oTime2: #if listed user time or open time or after it
                        if time < cTime2: #and if user time is before close time
                            oTime2 = oTime2.strftime("%H:%M")
                            cTime2 = cTime2.strftime("%H:%M")
                            open_rests.append("{} is open from {} to {}".format(restaurant, oTime1,cTime1))


        #Check if list of open retaurants is populated to print it otherwise indicated that none is open at the time.
        if len(open_rests) >= 1:
                time = time.strftime("%H:%M")
                print("We found {} open restaurant(s)".format(len(open_rests)))
                print("The following restaurants are open at {} on {}".format(time, userDay))
                for line in open_rests:
                    print(line, "\n")
        else:
            print("No restraunt is open by {} on {}".format(time, userDay))
    except:
        print("That's not a valid time. Please try again in this format HH:MM")
    else:
        print("We will need the time as numbers.")

if __name__ == find_open_restaurants():
    find_open_restaurants()
