from tkinter import *

root = Tk()
root.title("Newspaper")
l3 = Label(root,text='''Wednesday\n4 September 2024''')
l2 = Label(root,text="Modern Times of Hindustan",font = "TimeNewRoman  30  bold")
l4 = Label(root,text=" ",bg="black")
l1 = Label(text='''What is a newspaper?
A newspaper is a scheduled publication that contains news of current events,\ninformative articles, diverse features, and advertising.
It is usually printed on low-grade, inexpensive paper, such as newsprint.
What is an Online Newspaper?
An online newspaper is the online version of a newspaper, either as a stand-alone\n publication or as the online version of a printed periodical.

History of Online Newspaper
An early example of an "online-only" newspaper or magazine was (PLATO) News Report,\n an online newspaper created by Bruce Parrello in 1974 on the PLATO System\n at the University of Illinois.In 1987, the Brazilian newspaper Jornaldodia\n ran on the state-owned Embratel network,moving to the Internet in the 1990s. By the late 1990s,\n hundreds of U.S. newspapers published online versions but\n did not yet offer much interactivity.One example is Britain's \nWeekend City Press Review, which provided a weekly news \nsummary online in 1995. Today, online news has become a\n huge part of society, leading people to argue whether \nor not it is good for society.Austra Taylor, author of the popular\n book The People's Platform, argues that online\n news does not provide the details needed to understand \nwhat happened fully. It is more just a quick summary \nto inform people what happened but does not give \na solution or fixation to the problem.

The First Online Newspapers
News has been online since the 1970s. The first newspaper service on America Online was
launched by the Chicago Tribune in May 1992. But not until 1995 was the online newspaper
concept of today developed, featuring among others CNN as a global news engine. Six years
later, in April 2001, American trade journal Editor & Publisher Interactive had registered
in its database 12,878 news media online. 1995 was the year in which public Internet usage
had its breakthrough in entire Western world, largely due to a simpler “point-and-click” 
interface for the World Wide 284 Web. 

For our E-edition read page 3
Continued...''',bg = "light yellow", fg = "Black" , font = "TimeNewRoman  12  bold")
l2.pack(fill=X)
l3.pack(anchor="n",fill=X)
l4.pack(fill=X)
l1.pack(fill=X)
root.mainloop()