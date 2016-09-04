delete from variable;
delete from Game_Question;
delete from Game_QuestionChoices;


insert into Game_Question(question_text) values ("Look at this series: 2, 1, (1/2), (1/4), ... What number should come next?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","(1/3)",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","(1/8)",1 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","(2/8)",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D"."(1/16",0 from variables;

delete from variable;


insert into Game_Question(question_text) values ("Look at this series: 1.5, 2.3, 3.1, 3.9, ... What number should come next?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","4.2",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","4.4",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","4.7",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","5.1",0 from variables;

insert into Game_Question(question_text) values ("Look at this series: 544, 509, 474, 439, ... What number should come next?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","404",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","414",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","420",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","445",0 from variables;

insert into Game_Question(question_text) values ("Look at this series: F2, __, D8, C16, B32, ... What number should fill the blank?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","A16",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","G4",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","E4",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","E3",0 from variables;

insert into Game_Question(question_text) values ("Look at this series: 664, 332, 340, 170, ____, 89, ... What number should fill the blank?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","85",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","97",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","109",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","178",0 from variables;

insert into Game_Question(question_text) values ("Look at this series: 8, 43, 11, 41, __, 39, 17, ... What number should fill in the blank?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","8",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","14",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","43",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","44",0 from variables;

insert into Game_Question(question_text) values ("Which word does NOT belong with the others?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","inch",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","ounce",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","centimeter",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","yard",0 from variables;

insert into Game_Question(question_text) values ("Which word does NOT belong with the others?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","rye",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","sourdough",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","wheat",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","loaf",0 from variables;

insert into Game_Question(question_text) values ("Which word does NOT belong with the others?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","rug",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","couch",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","stool",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","chair",0 from variables;

insert into Game_Question(question_text) values ("Which word does NOT belong with the others?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","unimportant",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","trivial",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","insignificant",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","familiar",0 from variables;

insert into Game_Question(question_text) values ("Which word does NOT belong with the others?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","unique",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","beautiful",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","rare",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","exceptional",0 from variables;

insert into Game_Question(question_text) values ("Odometer is to mileage as compass is to");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","speed",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","hiking",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","needle",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","direction",0 from variables;

insert into Game_Question(question_text) values ("Marathon is to race as hibernation is to");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","winter",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","bear",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","dream",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","sleep",0 from variables;

insert into Game_Question(question_text) values ("Cup is to coffee as bowl is to");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","dish",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","soup",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","spoon",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","food",0 from variables;

insert into Game_Question(question_text) values ("Optimist is to cheerful as pessimist is to");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","gloomy",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","mean",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","petty",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","helpful",0 from variables;

insert into Game_Question(question_text) values ("Sponge is to porous as rubber is to");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","massive",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","solid",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","elastic",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","inflexible",0 from variables;

insert into Game_Question(question_text) values ("Applying for Seasonal Employment occurs when a person requests to be considered for a job that is dependent on a particular season or time of year. Which situation below is the best example of Applying for Seasonal Employment?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","The ski instructors at Top of the Peak Ski School work from December through March.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","Matthew prefers jobs that allow him to work outdoors.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","Lucinda makes an appointment with the beach resort restaurant manager to interview for the summer waitressing position that was advertised in the newspaper.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","Dougs ice cream shop stays open until 11 p.m. during the summer months.",0 from variables;

insert into Game_Question(question_text) values ("Violating an Apartment Lease occurs when a tenant does something prohibited by the legally binding document that he or she has signed with a landlord. Which situation below is the best example of Violating an Apartment Lease?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","Tim has decided to move to another city, so he calls his landlord to tell him that he is not interested in renewing his lease when it expires next month.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","Valerie recently lost her job and, for the last three months, has neglected to pay her landlord the monthly rent they agreed upon in writing when she moved into her apartment eight months ago.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","Mark writes a letter to his landlord that lists numerous complaints about the apartment he has agreed to rent for two years.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","Leslie thinks that her landlord is neglecting the building in which she rents an apartment. She calls her attorney to ask for advice.",0 from variables;

insert into Game_Question(question_text) values ("An Informal Gathering occurs when a group of people get together in a casual, relaxed manner. Which situation below is the best example of an Informal Gathering?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","The book club meets on the first Thursday evening of every month.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","After finding out about his promotion, Jeremy and a few coworkers decide to go out for a quick drink after work.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","Mary sends out 25 invitations for the bridal shower she is giving for her sister.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","Whenever she eats at the Mexican restaurant, Clara seems to run into Peter.",0 from variables;

insert into Game_Question(question_text) values ("The rules of baseball state that a batter Legally Completes His Time at Bat when he is put out or becomes a base runner. Which situation below is the best example of a batter Legally Completing His Time at Bat?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","Jared's blooper over the head of the short-stop puts him in scoring position.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","The umpire calls a strike, even though the last pitch was way outside.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","The pitcher throws his famous knuckleball, Joe swings and misses, and the umpire calls a strike.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","The count is two balls and two strikes as Mario waits for the next pitch.",0 from variables;

insert into Game_Question(question_text) values ("Vincent has a paper route. Each morning, he delivers 37 newspapers to customers in his neighborhood. It takes Vincent 50 minutes to deliver all the papers. If Vincent is sick or has other plans, his friend Thomas, who lives on the same street, will sometimes deliver the papers for him.");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","Vincent and Thomas live in the same neighborhood.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","It takes Thomas more than 50 minutes to deliver the papers.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","It is dark outside when Vincent begins his deliveries.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","Thomas would like to have his own paper route.",0 from variables;

insert into Game_Question(question_text) values ("The Pacific yew is an evergreen tree that grows in the Pacific Northwest. The Pacific yew has a fleshy, poisonous fruit. Recently, taxol, a substance found in the bark of the Pacific yew, was discovered to be a promising new anticancer drug.");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","Taxol is poisonous when taken by healthy people.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","Taxol has cured people from various diseases.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","People should not eat the fruit of the Pacific yew.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","The Pacific yew was considered worthless until taxol was discovered.",0 from variables;

insert into Game_Question(question_text) values ("Erin is twelve years old. For three years, she has been asking her parents for a dog. Her parents have told her that they believe a dog would not be happy in an apartment, but they have given her permission to have a bird. Erin has not yet decided what kind of bird she would like to have.");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","Erin's parents like birds better than they like dogs.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","Erin does not like birds.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","Erin and her parents live in an apartment.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","Erin and her parents would like to move.",0 from variables;

insert into Game_Question(question_text) values ("Tim's commute never bothered him because there were always seats available on the train and he was able to spend his 40 minutes comfortably reading the newspaper or catching up on paperwork. Ever since the train schedule changed, the train has been extremely crowded, and by the time the doors open at his station, there isn't a seat to be found.");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","Tim would be better off taking the bus to work.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","Tims commute is less comfortable since the train schedule changed.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","Many commuters will complain about the new train schedule.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","Tim will likely look for a new job closer to home.",0 from variables;

insert into Game_Question(question_text) values ("When they heard news of the hurricane, Maya and Julian decided to change their vacation plans. Instead of traveling to the island beach resort, they booked a room at a fancy new spa in the mountains. Their plans were a bit more expensive, but they had heard wonderful things about the spa and they were relieved to find availability on such short notice.");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","Maya and Julian take beach vacations every year.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","The spa is overpriced.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","It is usually necessary to book at least six months in advance at the spa.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","Maya and Julian decided to change their vacation plans because of the hurricane.",0 from variables;

insert into Game_Question(question_text) values ("Ten new television shows appeared during the month of September. Five of the shows were sitcoms, three were hour-long dramas, and two were news-magazine shows. By January, only seven of these new shows were still on the air. Five of the shows that remained were sitcoms.");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A","Only one of the news-magazine shows remained on the air.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B","Only one of the hour-long dramas remained on the air.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C","At least one of the shows that was cancelled was an hour-long drama.",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D","Television viewers prefer sitcoms over hour-long dramas.",0 from variables;

insert into Game_Question(question_text) values ("Here are some words translated from an artificial language.
gorblflur means fan belt
pixngorbl means ceiling fan
arthtusl means tile roof
Which word could mean 'ceiling tile'?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A", "gorbltusl",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B", "flurgorbl",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C", "arthflur",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D", "pixnarth",0 from variables;

insert into Game_Question(question_text) values ("Here are some words translated from an artificial language.
hapllesh means cloudburst
srenchoch means pinball
resbosrench means ninepin
Which word could mean 'cloud nine'?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A", "srensrench",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B", "ochhapl",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C", "haploch",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D", "haplresbo",0 from variables;

insert into Game_Question(question_text) values ("Here are some words translated from an artificial language.
agnoscrenia means poisonous spider
delanocrenia means poisonous snake
agnosdeery means brown spider
Which word could mean 'black widow spider'?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A", "deeryclostagnos",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B", "agnosdelano",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C", "agnosvitriblunin",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D", "trymuttiagnos",0 from variables;

insert into Game_Question(question_text) values ("Here are some words translated from an artificial language.
moolokarn means blue sky
wilkospadi means bicycle race
moolowilko means blue bicycle
Which word could mean 'racecar'?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A", "wilkozwet",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B", "spadiwilko",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C", "moolobreil",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D", "spadivolo",0 from variables;

insert into Game_Question(question_text) values ("Here are some words translated from an artificial language.
migenlasan means cupboard
lasanpoen means boardwalk
cuopdansa means pullman
Which word could mean 'walkway'?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A", "poenmigen",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B", "cuopeisel",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C", "lasandansa",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D", "poenforc",0 from variables;

insert into Game_Question(question_text) values ("Here are some words translated from an artificial language.
godabim means kidney stones
romzbim means kidney beans
romzbako means wax beans
Which word could mean 'wax statue'?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A", "godaromz",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B", "lazbim",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C", "wasibako",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D", "romzpeo",0 from variables;

insert into Game_Question(question_text) values ("Here are some words translated from an artificial language.
granamelke means big tree
pinimelke means little tree
melkehoon means tree house
Which word could mean 'big house'?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A", "granahoon",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B", "pinishur",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C", "pinihoon",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D", "melkegrana",0 from variables;

insert into Game_Question(question_text) values ("Here are some words translated from an artificial language.
daftafoni means advisement
imodafta means misadvise
imolokti means misconduct
Which word could mean 'statement'?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A", "kratafoni",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B", "kratadafta",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C", "loktifoni",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D", "daftaimo",0 from variables;

insert into Game_Question(question_text) values ("Here are some words translated from an artificial language.
lelibroon means yellow hat
plekafroti means flower garden
frotimix means garden salad
Which word could mean 'yellow flower'?");
insert into variables(primary_key) values ( last_insert_rowid());
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "A", "lelifroti",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "B", "lelipleka",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "C", "plekabroon",0 from variables;
insert into Game_QuestionChoice(question_id,choice_code,choice_text,correct_choice) select primary_key, "D", "frotibroon",0 from variables;

insert into Game_Question(question_text) values ("Here are some words translated from an artificial language.
myncabel means saddle horse
conowir means trail ride
cabelalma means horse blanket
Which word could mean 'horse ride'?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	cabelwir
B.	conocabel
C.	almamyn
D.	conoalma

	
insert into Game_Question(question_text) values ("Here are some words translated from an artificial language.
dionot means oak tree
blyonot means oak leaf
blycrin means maple leaf
Which word could mean 'maple syrup'?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	blymuth
B.	hupponot
C.	patricrin
D.	crinweel

insert into Game_Question(question_text) values ("Here are some words translated from an artificial language.
tamceno means sky blue
cenorax means blue cheese
aplmitl means star bright
Which word could mean 'bright sky'?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	cenotam
B.	mitltam
C.	raxmitl
D.	aplceno

insert into Game_Question(question_text) values ("Eileen is planning a special birthday dinner for her husband's 35th birthday. She wants the evening to be memorable, but her husband is a simple man who would rather be in jeans at a baseball game than in a suit at a fancy restaurant. Which restaurant below should Eileen choose?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	Alfredo's offers fine Italian cuisine and an elegant Tuscan decor. Patrons will feel as though they've spent the evening in a luxurious Italian villa.
B.	Pancho's Mexican Buffet is an all-you-can-eat family style smorgasbord with the best tacos in town.
C.	The Parisian Bistro is a four-star French restaurant where guests are treated like royalty. Chef Dilbert Olay is famous for his beef bourguignon.
D.	Marty's serves delicious, hearty meals in a charming setting reminiscent of a baseball clubhouse in honor of the owner,Marty Lester, a former major league baseball all-star.

insert into Game_Question(question_text) values ("The school principal has received complaints from parents about bullying in the school yard during recess. He wants to investigate and end this situation as soon as possible, so he has asked the recess aides to watch closely. Which situation should the recess aides report to the principal?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	A girl is sitting glumly on a bench reading a book and not interacting with her peers.
B.	Four girls are surrounding another girl and seem to have possession of her backpack.
C.	Two boys are playing a one-on-one game of basketball and are arguing over the last basket scored.
D.	Three boys are huddled over a handheld video game, which is not supposed to be on school grounds.

insert into Game_Question(question_text) values ("Mrs. Carson took a taxi to meet her three friends for lunch. They were waiting for her outside the restaurant when she pulled up in the car. She was so excited to see her friends that she left her tote bag in the taxi. As the taxi pulled away, she and her friends took notice of the license plate number so they would be able to identify the car when they called the taxi company.
#1: The four women seem to agree that the plate starts out with the letter J.
#2: Three of them agree that the plate ends with 12L.
#3: Three of them think that the second letter is X, and a different three think that the third letter is K.
The four license plate numbers below represent what each of the four women thinks she saw. Which one is most likely the license plate number of the taxi?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	JXK 12L
B.	JYK 12L
C.	JXK 12I
D.	JXX 12L

insert into Game_Question(question_text) values ("Zachary has invited his three buddies over to watch the basketball game on his wide-screen television. They are all hungry, but no one wants to leave to get food. Just as they are arguing about who should make the food run, a commercial comes on for a local pizze-ria that delivers. The phone number flashes on the screen briefly and they all try to remember it. By the time Zachary grabs a pen and paper, each of them recollects a different number.
#1: All of the men agree that the first three numbers are 995.
#2: Three of them agree that the fourth number is 9.
#3: Three agree that the fifth number is 2.
#4: Three agree that the sixth number is 6; three others agree that the seventh number is also 6.
Which of the numbers is most likely the telephone number of the pizzeria?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	995-9266
B.	995-9336
C.	995-9268
D.	995-8266

insert into Game_Question(question_text) values ("Mark is working with a realtor to find a location for the toy store he plans to open in his town. He is looking for a place that is either in, or not too far from, the center of town and one that would attract the right kind of foot traffic. Which of the following locations should Mark's realtor call to his attention?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	a storefront in a new high-rise building near the train station in the center of town whose occupants are mainly young, childless professionals who use the train to commute to their offices each day.
B.	a little shop three blocks away from the town's main street, located across the street from an elementary school and next door to an ice cream store
C.	a stand-alone storefront on a quiet residential street ten blocks away from the town's center
D.	a storefront in a small strip mall located on the outskirts of town that is also occupied by a pharmacy and a dry cleaner

insert into Game_Question(question_text) values ("Rita, an accomplished pastry chef who is well known for her artistic and exquisite wedding cakes, opened a bakery one year ago and is surprised that business has been so slow. A consultant she hired to conduct market research has reported that the local population doesn't think of her shop as one they would visit on a daily basis but rather a place they'd visit if they were celebrating a special occasion. Which of the following strategies should Rita employ to increase her daily business?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	making coupons available that entitle the coupon holder to receive a 25% discount on wedding, anniversary, or birthday cakes
B.	exhibiting at the next Bridal Expo and having pieces of one of her wedding cakes available for tasting
C.	placing a series of ads in the local newspaper that advertise the wide array of breads
D.	moving the bakery to the other side of town

insert into Game_Question(question_text) values ("Dr. Miller has a busy pediatric dentistry practice and she needs a skilled, reliable hygienist to keep things running smoothly. The last two people she hired were recommended by top dentists in the area, but they each lasted less than one month. She is now in desperate need of a hygienist who can competently handle the specific challenges of her practice. Which one of the following candidates should Dr. Miller consider most seriously?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	Marilyn has been a hygienist for fifteen years, and her current employer, who is about to retire, says she is the best in the business. The clientele she has worked with consists of some of the wealthiest and most powerful citizens in the county.
B.	Lindy recently graduated at the top of her class from one of the best dental hygiene programs in the state. Prior to becoming a dental hygienist, Lindy spent two years working in a day care center.
C.	James has worked as a dental hygienist for three years in a public health clinic. He is very interested in securing a position in a private dental office.
D.	Kathy is an experienced and highly recommended dental hygienist who is also finishing up a degree in early childhood education, which she hopes will get her a job as a preschool teacher. She is eager to find a job in a pediatric practice, since she has always wanted to work with children.

insert into Game_Question(question_text) values ("Mrs. Jansen recently moved to Arizona. She wants to fill her new backyard with flowering plants. Although she is an experienced gardener, she isn't very well-versed in what plants will do well in the Arizona climate. Also, there is a big tree in her backyard making for shady conditions and she isn't sure what plants will thrive without much direct sunlight. Her favorite gardening catalog offers several backyard seed packages. Which one should Mrs. Jansen choose?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	The Rainbow Collection is ideal for North-east gardens. It includes a variety of colorful perennials that thrive in cool, moist conditions.
B.	The Greenhouse Collection will blossom year after year if planted in brightly lit locations and watered regularly.
C.	The Treehouse Collection will provide lush green plants with delicate colorful flowers that thrive in shady and partially shady locations.
D.	The Oasis Collection includes a variety of perennials that thrive in dry climates and bright sunlight.

insert into Game_Question(question_text) values ("Tanya is older than Eric.
Cliff is older than Tanya.
Eric is older than Cliff.
If the first two statements are true, the third statement is");
insert into variables(primary_key) values ( last_insert_rowid());
A.	true
B.	false
C.	uncertain

insert into Game_Question(question_text) values ("Blueberries cost more than strawberries.
Blueberries cost less than raspberries.
Raspberries cost more than strawberries and blueberries.
If the first two statements are true, the third statement is");
insert into variables(primary_key) values ( last_insert_rowid());
A.	true
B.	false
C.	uncertain

insert into Game_Question(question_text) values ("All the trees in the park are flowering trees.
Some of the trees in the park are dogwoods.
All dogwoods in the park are flowering trees.
If the first two statements are true, the third statement is");
insert into variables(primary_key) values ( last_insert_rowid());
A.	true
B.	false
C.	uncertain

insert into Game_Question(question_text) values ("Mara runs faster than Gail.
Lily runs faster than Mara.
Gail runs faster than Lily.
If the first two statements are true, the third statement is");
insert into variables(primary_key) values ( last_insert_rowid());
A.	true
B.	false
C.	uncertain

insert into Game_Question(question_text) values ("Apartments in the Riverdale Manor cost less than apartments in The Gaslight Commons.
Apartments in the Livingston Gate cost more than apartments in the The Gaslight Commons.
Of the three apartment buildings, the Livingston Gate costs the most.
If the first two statements are true, the third statement is");
insert into variables(primary_key) values ( last_insert_rowid());
A.	true
B.	false
C.	uncertain

insert into Game_Question(question_text) values ("The Kingston Mall has more stores than the Galleria.
The Four Corners Mall has fewer stores than the Galleria.
The Kingston Mall has more stores than the Four Corners Mall.
If the first two statements are true, the third statement is");
insert into variables(primary_key) values ( last_insert_rowid());
A.	true
B.	false
C.	uncertain

insert into Game_Question(question_text) values ("All the tulips in Zoe's garden are white.
All the pansies in Zoe's garden are yellow.
All the flowers in Zoe's garden are either white or yellow
If the first two statements are true, the third statement is");
insert into variables(primary_key) values ( last_insert_rowid());
A.	true
B.	false
C.	uncertain

insert into Game_Question(question_text) values ("During the past year, Josh saw more movies than Stephen.
Stephen saw fewer movies than Darren.
Darren saw more movies than Josh.
If the first two statements are true, the third statement is");
insert into variables(primary_key) values ( last_insert_rowid());
A.	true
B.	false
C.	uncertain

insert into Game_Question(question_text) values ("Rover weighs less than Fido.
Rover weighs more than Boomer.
Of the three dogs, Boomer weighs the least.
If the first two statements are true, the third statement is");
insert into variables(primary_key) values ( last_insert_rowid());
A.	true
B.	false
C.	uncertain

insert into Game_Question(question_text) values ("All the offices on the 9th floor have wall-to-wall carpeting.
No wall-to-wall carpeting is pink.
None of the offices on the 9th floor has pink wall-to-wall carpeting.
If the first two statements are true, the third statement is");
insert into variables(primary_key) values ( last_insert_rowid());
A.	true
B.	false
C.	uncertain

insert into Game_Question(question_text) values ("One New York publisher has estimated that 50,000 to 60,000 people in the United States want an anthology that includes the complete works of William Shakespeare. And what accounts for this renewed interest in Shakespeare? As scholars point out, his psychological insights into both male and female characters are amazing even today.
This paragraph best supports the statement that");
insert into variables(primary_key) values ( last_insert_rowid());
A.	Shakespeares characters are more interesting than fictional characters today.
B.	people even today are interested in Shakespeare's work because of the characters.
C.	academic scholars are putting together an anthology of Shakespeare's work.
D.	New Yorkers have a renewed interested in the work of Shakespeare.
E.	Shakespeare was a psychiatrist as well as a playwright.

insert into Game_Question(question_text) values ("One of the warmest winters on record has put consumers in the mood to spend money. Spending is likely to be the strongest in thirteen years. During the month of February, sales of existing single-family homes hit an annual record rate of 4.75 million.
This paragraph best supports the statement that");
insert into variables(primary_key) values ( last_insert_rowid());
A.	consumer spending will be higher thirteen years from now than it is today.
B.	more people buy houses in the month of February than in any other month.
C.	during the winter months, the prices of single-family homes are the lowest.
D.	there were about 4 million homes for sale during the month of February.
E.	warm winter weather is likely to affect the rate of home sales.

insert into Game_Question(question_text) values ("Generation Xers are those people born roughly between 1965 and 1981. As employees, Generation Xers tend to be more challenged when they can carry out tasks independently. This makes Generation Xers the most entrepreneurial generation in history.
This paragraph best supports the statement that Generation Xers");
insert into variables(primary_key) values ( last_insert_rowid());
A.	work harder than people from other generations.
B.	have a tendency to be self-directed workers
C.	have an interest in making history
D.	tend to work in jobs that require risk-taking behavior.
E.	like to challenge their bosses work attitudes.

insert into Game_Question(question_text) values ("If you're a fitness walker, there is no need for a commute to a health club. Your neighborhood can be your health club. You don't need a lot of fancy equipment to get a good workout either. All you need is a well-designed pair of athletic shoes.
This paragraph best supports the statement that");
insert into variables(primary_key) values ( last_insert_rowid());
A.	fitness walking is a better form of exercise than weight lifting.
B.	a membership in a health club is a poor investment.
C.	walking outdoors provides a better workout than walking indoors.
D.	fitness walking is a convenient and valuable form of exercise.
E.	poorly designed athletic shoes can cause major foot injuries.

insert into Game_Question(question_text) values ("In the past, consumers would rarely walk into an ice cream store and order low-fat ice cream. But that isn't the case today. An increasing health consciousness combined with a much bigger selection of tasty low-fat foods in all categories has made low-fat ice cream a very profitable item for ice cream store owners.
This paragraph best supports the statement that");
insert into variables(primary_key) values ( last_insert_rowid());
A.	low-fat ice cream produces more revenue than other low-fat foods.
B.	ice cream store owners would be better off carrying only low-fat ice cream.
C.	ice cream store owners no longer think that low-fat ice cream is an unpopular item.
D.	low-fat ice cream is more popular than other kinds of ice cream.
E.	consumers are fickle and it is impossible to please them

insert into Game_Question(question_text) values ("Today's high school students spend too much time thinking about trivial and distracting matters such as fashion. Additionally, they often dress inappropriately on school grounds. Rather than spending time writing another detailed dress policy, we should make school uniforms mandatory. If students were required to wear uniforms, it would increase a sense of community and harmony in our schools and it would instill a sense of discipline in our students. Another positive effect would be that teachers and administrators would no longer have to act as clothing police, freeing them up to focus on more important issues.
This paragraph best supports the statement that");
insert into variables(primary_key) values ( last_insert_rowid());
A.	inappropriate clothing leads to failing grades.
B.	students who wear school uniforms get into better colleges.
C.	teachers and administrators spend at least 25% of their time enforcing the dress code.
D.	students are not interested in being part of a community
E.	school uniforms should be compulsory for high school students.

insert into Game_Question(question_text) values ("The criminal justice system needs to change. The system could be more just if it allowed victims the opportunity to confront the person who has harmed them. Also, mediation between victims and their offenders would give the offenders a chance to apologize for the harm they have done.
This paragraph best supports the statement that victims of a crime should");
insert into variables(primary_key) values ( last_insert_rowid());
A.	learn to forgive their offenders.
B.	have the right to confront their offenders.
C.	learn the art of mediation.
D.	insist that their offenders be punished.
E.	have the right to impose a sentence on their offenders.

insert into Game_Question(question_text) values ("A few states in this country are considering legislation that would prohibit schools from using calculators before the sixth grade. Other states take a different position. Some states are insisting on the purchase of graphing calculators for every student in middle school.
This paragraph best supports the statement that in this country");
insert into variables(primary_key) values ( last_insert_rowid());
A.	there are at least two opinions about the use of calculators in schools.
B.	calculators are frequently a detriment to learning math.
C.	state legislators are more involved in education than ever before.
D.	the price of graphing calculators is less when schools buy in bulk.
E.	the argument against calculators in schools is unfounded.

insert into Game_Question(question_text) values ("Today's workforce has a new set of social values. Ten years ago, a manager who was offered a promotion in a distant city would not have questioned the move. Today, a manager in that same situation might choose family happiness instead of career advancement.
This paragraph best supports the statement that");
insert into variables(primary_key) values ( last_insert_rowid());
A.	most managers are not loyal to the corporations for which they work.
B.	businesses today do not understand their employees needs.
C.	employees social values have changed over the past ten years.
D.	career advancement is not important to todays business managers.
E.	companies should require their employees to accept promotions.

insert into Game_Question(question_text) values ("It is well known that the world urgently needs adequate distribution of food, so that everyone gets enough. Adequate distribution of medicine is just as urgent. Medical expertise and medical supplies need to be redistributed throughout the world so that people in emerging nations will have proper medical care.
This paragraph best supports the statement that");
insert into variables(primary_key) values ( last_insert_rowid());
A.	the majority of the people in the world have never been seen by a doctor.
B.	food production in emerging nations has slowed during the past several years.
C.	most of the worlds doctors are selfish about giving time and money to the poor.
D.	the medical-supply industry should step up production of its products.
E.	many people who live in emerging nations are not receiving proper medical care

insert into Game_Question(question_text) values ("Look at this series: 1.5, 2.3, 3.1, 3.9, ... What number should come next?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	4.2
B.	4.4
C.	4.7
D.	5.1

insert into Game_Question(question_text) values ("Look at this series: 14, 28, 20, 40, 32, 64, ... What number should come next?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	52
B.	56
C.	96
D.	128

insert into Game_Question(question_text) values ("Look at this series: 2, 4, 6, 8, 10, ... What number should come next?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	11
B.	12
C.	13
D.	14

insert into Game_Question(question_text) values ("Look at this series: 201, 202, 204, 207, ... What number should come next?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	205
B.	208
C.	210
D.	211

insert into Game_Question(question_text) values ("Look at this series: 544, 509, 474, 439, ... What number should come next?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	404
B.	414
C.	420
D.	445

insert into Game_Question(question_text) values ("Look at this series: 80, 10, 70, 15, 60, ... What number should come next?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	20
B.	25
C.	30
D.	50

insert into Game_Question(question_text) values ("Look at this series: 2, 6, 18, 54, ... What number should come next?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	108
B.	148
C.	162
D.	216

insert into Game_Question(question_text) values ("Look at this series: 5.2, 4.8, 4.4, 4, ... What number should come next?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	3
B.	3.3
C.	3.5
D.	3.6

insert into Game_Question(question_text) values ("Look at this series: 8, 6, 9, 23, 87 , ... What number should come next?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	128
B.	226
C.	324
D.	429

insert into Game_Question(question_text) values ("It is appropriate to compensate someone if you have damaged his or her property in some way. This is called Restitution. Which situation below is the best example of Restitution?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	Jake borrows Leslie's camera and the lens shatters when it falls on the ground because he fails to zipper the case.When Jake returns the camera, he tells Leslie that he will pay for the repair.
B.	Rebecca borrows her neighbor's car, and when she returns it, the gas tank is practically empty. She apologizes profusely and tells her neighbor she will be more considerate the next time.
C.	Aaron asks Tom to check in on his apartment while he is out of town. When Tom arrives, he discovers that a pipe has burst and there is a considerable amount of water damage. He calls a plumber to repair the pipe.
D.	Lisa suspects that the pothole in her companys parking lot caused her flat tire. She tells her boss that she thinks the company should pay for the repair.

insert into Game_Question(question_text) values ("Reentry occurs when a person leaves his or her social system for a period of time and then returns. Which situation below best describes Reentry ?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	When he is offered a better paying position, Jacob leaves the restaurant he manages to manage a new restaurant on the other side of town.
B.	Catherine is spending her junior year of college studying abroad in France.
C.	Malcolm is readjusting to civilian life after two years of overseas military service.
D.	After several miserable months, Sharon decides that she can no longer share an apartment with her roommate Hilary.

insert into Game_Question(question_text) values ("Embellishing the Truth occurs when a person adds fictitious details or exaggerates facts or true stories. Which situation below is the best example of Embellishing the Truth?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	Isabel goes to the theater, and the next day, she tells her coworkers she thought the play was excellent.
B.	The realtor describes the house, which is eleven blocks away from the ocean, as prime waterfront property.
C.	During the job interview, Fred, who has been teaching elementary school for ten years, describes himself as a very experienced teacher.
D.	The basketball coach says it is likely that only the most talented players will get a college scholarship.

insert into Game_Question(question_text) values ("Establishing a Power of Attorney occurs when a legal document is created that gives one individual the authority to act for another. Which situation below is the best example of Establishing a Power of Attorney?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	Louise is selling her house and she hires a lawyer to review the contract.
B.	Simones mother can no longer get to the bank to cash her checks and make deposits, so she has taken legal steps to enable Simone to do these things for her.
C.	Jack's father is elderly and Jack thinks he is no longer able to make decisions for himself.
D.	At her daughter's urging, Mrs.Lenox opens up a retirement account with the local bank.

insert into Game_Question(question_text) values ("Artist is to painting as senator is to");
insert into variables(primary_key) values ( last_insert_rowid());
A.	attorney
B.	law
C.	politician
D.	constituents

insert into Game_Question(question_text) values ("Exercise is to gym as eating is to");
insert into variables(primary_key) values ( last_insert_rowid());
A.	food
B.	dieting
C.	fitness
D.	restaurant

insert into Game_Question(question_text) values ("Candid is to indirect as honest is to");
insert into variables(primary_key) values ( last_insert_rowid());
A.	frank
B.	wicked
C.	truthful
D.	untruthful

insert into Game_Question(question_text) values ("Guide is to direct as reduce is to");
insert into variables(primary_key) values ( last_insert_rowid());
A.	decrease
B.	maintain
C.	increase
D.	preserve

insert into Game_Question(question_text) values ("Oar is to rowboat as foot is to");
insert into variables(primary_key) values ( last_insert_rowid());
A.	running
B.	sneaker
C.	skateboard
D.	jumping

insert into Game_Question(question_text) values ("7 - 4 x 3 is equal to");
insert into variables(primary_key) values ( last_insert_rowid());
A.	9
B.	-5
C.	-4
D.	19

insert into Game_Question(question_text) values ("18 - (5 x 4 - 2) is equal to");
insert into variables(primary_key) values ( last_insert_rowid());
A.	8
B.	21
C.	-4
D.	0

insert into Game_Question(question_text) values ("4 x 3 + 7 x 9 is equal to ");
insert into variables(primary_key) values ( last_insert_rowid());
A.	49
B.	171
C.	75
D. 	64

insert into Game_Question(question_text) values ("Which word does NOT belong with the others?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	scythe
B.	knife
C.	pliers
D.	saw

insert into Game_Question(question_text) values ("Which word does NOT belong with the others?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	biology
B.	chemistry
C.	theology
D.	zoology

insert into Game_Question(question_text) values ("Which word does NOT belong with the others?");
insert into variables(primary_key) values ( last_insert_rowid());
A.	evaluate
B.	assess
C.	appraise
D.	instruct
