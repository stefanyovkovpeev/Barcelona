import sqlite3


conn = sqlite3.connect("SQL3DB.db")


cursor = conn.cursor()


cursor.execute("SELECT * FROM alllocations")
alllocations={}

for x in cursor:
    alllocations[x[0]]=[x[1],x[2]]

cursor.execute("select * from allnavigations")
allnavigations={}

for x in cursor:
    if len(x)==5:
     allnavigations[x[0]]=[x[1],x[2],x[3],x[4]]
    else:
     allnavigations[x[0]] = [x[1], x[2], x[3], None]

cursor.execute("select * from restaurants")
restaurant_data = []

for x in cursor:
    restaurant_data_dic = {"name": x[0],"image": x[1],"info": x[2]}
    restaurant_data.append(restaurant_data_dic)

cursor.execute("select * from clubs")
clubs_data = []

for x in cursor:
    clubs_data_dic = {"name": x[0],"image": x[1],"info": x[2]}
    clubs_data.append(clubs_data_dic)
#at first all the values were hardcoded - heres the values and the code to get it to the DB

# alllocations = {'Акта Атриум Хотел': ["Pictures/АктаАтриум.png",
#                                      "Този елегантен хотел се намира на 250 метра от метростанция и булевард Paseo de Gracia. Площад „Каталуния“ е на 5 минути пеша. Осигурен е безплатен WiFi.Хотел Acta Atrium Palace се помещава в красива сграда от 1888-ма година. Предлага модерни и елегантни стаи с климатик, телевизор със сателитни канали и собствена баня с безплатни тоалетни принадлежности и халат.На разположение е денонощен румсървис.Известните сгради Casa Batlló и La Pedrera на архитекта Гауди са на 10 минути пеша. Има денонощна рецепция и туристическо бюро, където се отдават автомобили под наем. Наблизо може да се ползва обществен паркинг."],
#                 'Парк"Лабиринт на Хорта"': ["Pictures/Labyrinth.jpg",
#                                             "Разположен на склона на Колсерола, лабиринтът Орта е проектиран през 1791 г. по изричното желание на Джоан Антони Десвалс, маркиз от Лупия, Ел Поал и Алфарас, на земя, принадлежаща на това благородно семейство. Любител на изкуството и природата, той искаше да създаде неокласическа градина с помощта на архитекта Доменико Багути и градинаря Джозеф Делвалет, вдъхновен от мита за Тезей: който успее да стигне до центъра, ще намери любовта като награда.През 1968 г. семейство Десвалс го дава на градския съвет, който след извършване на различни възстановителни работи го отваря за обществеността през 1971 г. Прекомерният приток на посетители от 70-те години причинява деградация на някои декоративни елементи и растения, поради което отново се реформира и той беше отворен отново с ограничен капацитет от 750 души наведнъж, за да се избегне постепенното му унищожаване."],
#                 'Парк"Гуел"': ["Pictures/Гуел.png",
#                                "Паркът Гуел е построен през периода 1900 – 1914 г. от Антонио Гауди по поръчка на граф Еузебио Гуел. Първоначалният план включвал строежа на 60 еднофамилни къщи, от които обаче са построени само две, една от които е превърната в музей на Гауди. От 1923 г. този парк е собственост на общината. При входа на парка ви посрещат голямото стълбище и талисманът на града – пъстрият мозаечен дракон. Изкачвайки се по стълбите ще се изправите пред огромни дорийски колони и площад, където според оригиналния план е трябвало да има пазар. Над него е обширната тераса, оградена от известната змиевидна пейка с разноцветен фаянс. Около тях, потънал в атмосфера на тишина и спокойствие, остава естествения парк и криволичещите му пътечки. Днес паркът е обявен за паметник от световно значение и е под защитата на ЮНЕСКО."],
#                 'Каса Висенс': ("Pictures/Висенс.png",
#                                 "Каса Висенс (от испански casa – „къща”) е първата къща, проектирана от испанския архитект от Каталуния Антонио Гауди (1852 – 1926). Той е един от най-големите новатори в областта на архитектурата по онова време и дълго след това. Характерният му индивидуален еклектичен стил, описван като смесица от неоготика и ар нуво, носи и белези на сюрреализма и кубизма. Като водеща при него се посочва испанската разновидност на ар нуво, наричана Каталонски модернизъм.Построена между 1883 и 1885 г. като лятна къща за семейство Висенс, още с този свой проект Гауди демонстрира несравнимия си талант въпреки липсата на опит по това време.На по малко от 10 минути пеш можете да се насладите и на останалите архитектурни творби на Гауди като къща Падуа и Мила."),
#                 'Къщите': ("Pictures/Висенс.png",
#                                 "Каса Висенс (от испански casa – „къща”) е първата къща, проектирана от испанския архитект от Каталуния Антонио Гауди (1852 – 1926). Той е един от най-големите новатори в областта на архитектурата по онова време и дълго след това. Характерният му индивидуален еклектичен стил, описван като смесица от неоготика и ар нуво, носи и белези на сюрреализма и кубизма. Като водеща при него се посочва испанската разновидност на ар нуво, наричана Каталонски модернизъм.Построена между 1883 и 1885 г. като лятна къща за семейство Висенс, още с този свой проект Гауди демонстрира несравнимия си талант въпреки липсата на опит по това време.На по малко от 10 минути пеш можете да се насладите и на останалите архитектурни творби на Гауди като къща Падуа и Мила."),
#                 'Мол Арена': ("Pictures/Аренас.png",
#                               "Историческата сграда, построена към края на 19 век, била изоставена през 70те години на миналия век главно поради спада в популярността на бикоборството в Каталония. Тъй като сградата е не само паметник на културата, но има и социално значение за града – не само като арена, но също така и сцена за опера, театър, рок концерти, политически събития и дори казарми през Гражданската Война – общинският съвет решава, че фасадата няма да бъде разрушена. Почти 47 000 кв.м. е площта на комплекса, като в сутерена е изграден паркинг с площ 1 250кв.м.Покривът и гигантската „чиния”, върху която е панорамната тераса, се поддържат от огромни пилони , като всички обслужващи помещения като ескалатори и стълбищни клетки са в зоната на пилона."),
#                 'Саграда Фамилия': ("Pictures/Саграда.png",
#                                     "Катедралата Саграда Фамилия е най-голямата християнска постройка в прослава на Светото семейство в Испания. Изключителна метафора на християнската религия. Проектът на катедралата включва три величествени фасади: източна, посветена на рождеството на Христос, западна – Страстите Христови, и южна – възхвала на името му, която е и най-голяма от всички. Всяка фасада има по четири кули, символизиращи дванадесетте апостоли. Заоблената кула във форма на купол над апсидата е символ на Божията майка. Четири големи кули, посветени на четиримата евангелисти, обграждат централната, най-висока кула, символизираща Спасителя. Катедралата е дело на 'любимия син на Барселона' - Антонио Гауди и е най-големият му проект. Той работи над него повече от 40 години. Гауди умира през 1926 г. преди да я завърши. Работата по завършването започва през 1978 г. Днес архитектът на катедралата е Жорди Бонет. Предполага се, че катедралата ще бъде напълно завършена едва през 22 век. Причина за продължителния период на дострояване е необходимостта от използване на традиционни и времеемки техники, наред със съвременните. Не трябва да се подминава и факта, че за завършването на катедралата все още се води ожесточена полемика между привържениците на тази идея и тези, които я отхвърлят."),
#                 'Ла Рамбла': ("Pictures/Ла Рамбла.png",
#                               "Ла Рамбла е широка и много дълга улица в Барселона или по-точно няколко улици свързани помежду си, на които центърът е даден изцяло на пешеходците, клоуните, мимовете, играчите, които правят трикове с футболни топки и изпълнители от всякакъв род. Всичко това и още много други, като будки за вестници, книги, места за хранене, магазини за птици с извадени навън клетки с най-различни крилати, както и магазини за цветя, които са изпъстрени със всички цветове на природата и много други видове магазини. Разглеждането на оживеният булевард Ла Рамбла кара човек да вникне в различни духовни измерения на Барселона от XXI век, а страничните му улички крият исторически и съвременни богатства във вдъхновяващ римейк от стилове. Ла Рамбла започва близо до Площад Каталуня, след което продължава и се извива по цялата дължина на Старата Барселона и свършва до паметника на Христофор Колумб и оживената пристанищна част.Площад “Каталуния” е сърцето на Барселона. Географският център на града е обозначен с голяма звезда на площада, но съществува опасност изобщо да не я забележите, освен ако не погледнете отвисоко. До 19 век тук не е имало нищо друго, освен няколко конюшни. С промяната на архитектурният план на града, мястото било планувано да се превърне в площад.Статуите, които днес са разположени около красивия фонтан са добавени по-късно, а многобройните гълъби създават неповторима атмосфера. Около площада ще откриете офиси на водещите испански банки, един от най-големите търговски центрове на Барселона - El Corte Ingles, многобройни ресторанти и барове (тук се намира и най-популярният бар на града – “Цюрих”), както и един от офисите за туристическа информация."),
#                 'Ла Рамбла и Площада': ("Pictures/Ла Рамбла.png",
#                               "Ла Рамбла е широка и много дълга улица в Барселона или по-точно няколко улици свързани помежду си, на които центърът е даден изцяло на пешеходците, клоуните, мимовете, играчите, които правят трикове с футболни топки и изпълнители от всякакъв род. Всичко това и още много други, като будки за вестници, книги, места за хранене, магазини за птици с извадени навън клетки с най-различни крилати, както и магазини за цветя, които са изпъстрени със всички цветове на природата и много други видове магазини. Разглеждането на оживеният булевард Ла Рамбла кара човек да вникне в различни духовни измерения на Барселона от XXI век, а страничните му улички крият исторически и съвременни богатства във вдъхновяващ римейк от стилове. Ла Рамбла започва близо до Площад Каталуня, след което продължава и се извива по цялата дължина на Старата Барселона и свършва до паметника на Христофор Колумб и оживената пристанищна част.Площад “Каталуния” е сърцето на Барселона. Географският център на града е обозначен с голяма звезда на площада, но съществува опасност изобщо да не я забележите, освен ако не погледнете отвисоко. До 19 век тук не е имало нищо друго, освен няколко конюшни. С промяната на архитектурният план на града, мястото било планувано да се превърне в площад.Статуите, които днес са разположени около красивия фонтан са добавени по-късно, а многобройните гълъби създават неповторима атмосфера. Около площада ще откриете офиси на водещите испански банки, един от най-големите търговски центрове на Барселона - El Corte Ingles, многобройни ресторанти и барове (тук се намира и най-популярният бар на града – “Цюрих”), както и един от офисите за туристическа информация."),
#                 'Замък Монтжуик': ("Pictures/Монтжуик.png",
#                                    "Монтжуик – именно от този хълм Дон Кихот е наблюдавал битката между флотата на християните и сарацините. Оттук, с помощта на съвършената за онова време система за сигнализация, състояща се от флагчета и сигнални огньове, се предавали съобщения на каталонските адмирали за местоположението на вражеските кораби.Височината на хълма е 213 м., пристанището е разположено непосредствено до него и до 1401 г. е служил като сигнален фар. Монтжуик е едно от най-интересните места в града. Монтжуик винаги е бил стратегически пункт за Барселона. През 1640 г., след войната срещу Фелипе IV, на върха на хълма е бил издигнат замък. След предаването на града в ръцете на Фелипе V Бурбонски, в края на войната за испанското наследство, замъкът е превърнат във военен затвор. Едва в наше време, в началото на 60-те години на миналия век, военните предават старинния замък на града и сега в него е открит военно-исторически музей.На хърма Манджуик се намира прекрасното етнографско селище Пуебло Еспаньол. Това е Испания, изобразена в миниатюра: градче, заемащо 2 хектара, с неговите улици, площади, домове и дворци, много точно възпроизвеждащи най-интересните и най-характерните области на тази голяма страна – Каталония, Арагон, Андалусия, Галисия, Кастилия, Балеарските острови, Навара и Естремадура."),
#                 'Триумфална Арка': ("Pictures/Арка.png",
#                                     "Набързо подготвеното Световно изложение през 1888 г. изисквало ( поне така смятали градските съветници) подобаващо величествен вход за официално посрещане . Архитектът Жозеп Виласека ( 1848 - 1910г.) създава тази изключително необичайна триумфална арка.Той загърбва класическите модели и камъка като материал и се насочва към ислямската традиция, установена в Испания преди векове, изграждайки арка от тухли. Идеята му да има кули от двете й страни е отхърлена. Много каталонски скулпори се включват ентусиазирано при декорацията на арката."),
#                 'Готически Квартал': ("Pictures/Готически.png",
#                                       "Добре дошли в Готическия квартал – вълшебно място в сърцето на Барселона. Този район е като машина на времето, която ви връща в Средновековието със своите тесни криволичещи улички и старинни сгради. Готическият квартал е изпълнен с история на всяка крачка.Готическият квартал, или „Бари Готик“, както го наричат местните, е една от най-старите части на Барселона. С високите си каменни сгради и калдъръмени улици той е като разходка из книга с приказки. Ще видите невероятни забележителности отпреди векове, които са непокътнати и днес.Разглеждането на Готическия квартал е като да се впуснете в приключение. Никога не знаеш на какво историческо съкровище ще се натъкнеш в следващия момент.Тук можете да намерите Катедралата, мостът на епископа, палатът на музиката и други."),
#                 'Парк Ситадела': ("Pictures/Ситадела.png",
#                                   "Градският парк на Барселона, наричан още 'Парк на Цитаделата', заради крепостта, която през 18 в. построил там Фелипе V, със своите 75 акрау градският парк е най-големият парк в Барселона. Завършен е през 1860 г., а интерес предизвиква факта, че в неговото проектиране е взел участие любимият архитект на Барселона – Гауди, който тогава е бил едва начинаещ. Разположен в източната част на стария град, недалече от олимпийското пристанище, със своите градини, езеро и цитрусови дръвчета, паркът е като оазис в модерния град. Тук се намира Зоологическата градина, Музеят на естествената история и Геоложкият музей. По-голяма част от сградите в парка са построени в чест на Световното изложение през 1888 г., както и Триумфалната арка на Барселона, разположена в непосредствена близост до парка. Срещу арката е и сградата на Парламента на Каталуния."),
#                 'Аквариумът на Барселона': ["Pictures/Аквариум.png",
#                                             "Аквариума на Барселона e един от най - големите в света. Той е разположен недалеч от яхтеното пристанище, в края на уживената търговска улица Ла Рамбла. Открит през 1995г., той потапя посетителите в разнообразието на живот на Средиземно море. Съставен е от над 35 раздела и повече от 11 000 обитатели от 450 различни вида. Аквариумът е разделен на няколко тематични зони - Средиземно море, Черно море, Антарктика и др.С най-големия средиземноморски тематичен аквариум в света, аквариумът в Барселона се състои от 80-метров тунел, в който живеят акули, змиорки, скатове и др. Най - голям интерес за посетителите представляват акулите. Една от предлаганите aтракции е гмуркане сред акули."],
#                 'Катедралата на Барселона': ["Pictures/Катедрала.png",
#                                              "Барселонската Катедрала, известна още като катедралата Ла Сеу, е прекрасен пример за каталонска готическа архитектура, датираща от XIV век, от чиито кули се вижда целия готически квартал в Барселона.Катедралата винаги е била духовен център на Барселона, който първо е бил римски храм, после зад стените й се е помещавала джамия, и накрая там витае християнския дух, превъплъщавайки се в църква.Строителството на катедралата започва през 1298 година по време на управлението на крал Хауме II и е завършена през 1448 година. Използвани са оригиналните чертежи на Шарл Галте от Руан от 1408 година, което води до визуална хармония в облика на катедралата. Смесването на средновековен и възрожденски стил в архитектурното бижу катедралата Ла Сеу, показват завършен вид на сградата с голяма камбанария, обхваната в готически зъбери, готически арки, красиво изваян хор и много параклиси.Особено забележителна е Капела де Сан Бенет, а в криптата зад олтара се намира впечатляващия саркофаг от алабастър на Санта Еулалия, покровителка на катедралата и на града. Девицата, дъщеря на семейство от висшата класа, е изгорена на клада от римляните заради убежденията си – счита се, че това е станало на 12 февруари 304 година."],
#                 'Дворец на каталунската музика': ["Pictures/Музика.png",
#                                                   "Това е първата музикална зала в града, която след създаването си се превръща в център на културните събития. Заради своята уникална архитектура, дело на архитекта Луис Монтенер, през 1997 г. тя е включена в списъка на ЮНЕСКО за световно наследство.В края на 19 в. каталунския регион е обзет от силен национализъм. Със своя уникален и вековен език и култура, както и със започването на модернистичното движение, местното население на Каталуния започва да иска независимост и признание от останалите държави.Архитектът Луис Монтенер, под чиито ръце е излезнал днешния дворец на Каталунската музика е деен участник в тази инициатива. Той и съмишлениците му, сред които не може да не се спомене и Антонио Гауди, искат да създадат уникален архитектурен вид на Барселона. Доказателство за това е сградата на Каталунската музика."],
#                 'Mercado de La Boqueria': ["Pictures/Букерия.png", "В Меркат де Sant Жозеп де ла Бокерия , често наричан просто Ла Бокерия ( каталонски:  [lə βukəɾi.ə] ; испански : La Boquería ), е голям обществен пазар в Ciutat Vella район на Барселона , Каталония , Испания , и една от най-големите туристически забележителности на града, с вход от La Rambla , недалеч от Liceu , операта на Барселона . Пазарът предлага много разнообразна селекция от стоки. Първото споменаване на пазара Boqueria в Барселона датира от 1217 г., когато в близост до старата градска порта са монтирани маси за продажба на месо. От декември 1470 г. на това място се провежда пазар за свине; по това време е бил известен като Mercadi Bornet. По-късно, до 1794 г., е известен просто като Mercat de la Palla или пазар за слама. В началото пазарът не беше затворен и нямаше официален статут, като се разглеждаше просто като продължение на пазара Plaça Nova , който се простираше до Plaça del Pi . Смята се, че настоящото име произлиза от каталунското boc , което означава „коза“, следователно boqueria би било място, където се продава козе месо ; сравнете също френскиboucherie , откъдето идва и Vucciria , името на пазар в Палермо , Италия. Първоначално той е построен в посвещение на двете най-големи легенди на Барселона, наречени Майра Селесте Родригес Монкада и Карлос Гонзалес. [ необходим е цитат ]По-късно властите решават да построят отделен пазар на Ла Рамбла , където се помещават основно рибарници и месари . Едва през 1826 г. пазарът е законно признат и конвенция, проведена през 1835 г., решава да изгради официална структура. Строителството започва на 19 март 1840 г. под ръководството на архитекта Мас Вила . Пазарът официално е открит през същата година, но плановете за сградата са многократно променяни. Откриването на структурата най-накрая се състоя през 1853 г. Нов рибен пазар е открит през 1911 г., а металният покрив, който все още съществува днес, е построен през 1914 г. "],
#                 'El Pont del Bisbe': ["Pictures/Мост.png",
#                                       "Едно от многото любопитни неща в готическия квартал е мостът на епископа с череп и кости. Зловеща легенда разказва, че всеки, който гледа директно към черепа, ще бъде прокълнат. За щастие, за повечето хора разходката по Carrer del Bisbe е шанс да избягат от натоварените тълпи на близките площади и да се възхитят от комбинацията от готически и неоготически елементи."],
#                 'Каса Падуа': ["Pictures/Падуа.png",
#                                "Построена през 1903, тази малка, бледо-зелена къщичка, с огнено-червени акценти, е представител на art nouveau архитектурата в Барселона.Къщата е дело на Jeroni Granell и до 1970 е била център на фабрика за парфюми.. като единственото нещо, което издава този факт, са може би флоралните елементи, разположени, по цялата фасада.Историята на Casa Padua е много оскъдна, изгубена или нарочно потулена, а самата тя е стояла дълго време изоставена, докато не бива реновирана от Alonso Balaguer, който дори печели награда за невероятните резултати, който постига."],
#                 'Каса Мила': ["Pictures/Мила.png",
#                               "Casa Mila е наричaна още La Pedrera (кариерата) заради интересната си форма, с която прилича на каменна кариера. Тя се намира на известния булевард Passaig de Gracia на ъгъла с Carrer de Provenca. Състои се от два свързани пететажни блока и е с обща площ 4500 кв.м. Всеки блок е построен около вътрешна градина, има свой собствен вход и общ подземен паркинг. Да, правилно прочетохте, годината е 1912, а хората могат да достигат с превозни средства директно до домовете си. Това е проектът, с който Гауди предизвиква истински фурор за своето време, а днес La Pedrera е една от топ забележителностите в Барселона."],
#                 'Плаж Сан Себастиан': ["Pictures/SanSebastian.png",
#                                        "Плажът Sant Sebastià се намира в Барселона, Каталуния, Испания. С 1100 метра, той е най-дългият в Барселона.Предлага живописни гледки плюс модерна статуя от Алфредо Ланц, посветена на плувните спортове.На него също се намира известния W hotel."],
#                 'Бус Турове': ["Pictures/BusTour.png", "Обиколката на града на Барселона е официална обиколка на Барселона с панорамна тераса, която предлага уникални гледки както към старата, така и към новата Барселона.Използвайки билета си толкова често, колкото пожелаете в рамките на един или два (последователни) дни, можете да се качвате и слизате на която и да е от 35-те спирки по нашите два маршрута, които разделят града на Зелен/Източен и Оранжев/Запад .Освен това, докато сте на борда на обиколката на Барселона, ще получите книга с отстъпка, която можете да използвате в ресторанти, магазини, обиколки с екскурзовод, транспорт и много други атракции.Автопарк от двуетажни автобуси.Barcelona City Tour разполага с флот от 40 двуетажни автобуса с панорамен горен етаж, предоставящ уникална гледка към града. Долната палуба е климатизирана и всички наши превозни средства са оборудвани с анатомични седалки, за да направят вашето пътуване по-комфортно. Не забравяйте, че целият ни автопарк е червен на цвят, което показва отпред кой маршрут се покрива във всеки един момент.За да гарантираме, че хората с ограничена подвижност също могат да се насладят на услугата, всички наши превозни средства са оборудвани с рампа за достъп до задната врата и място, отделено за инвалидни колички, непрекъсната платформа с нисък под и система за бързо накланяне, която накланя превозното средство надясно .За да се осигури гладко обслужване, всички пътници трябва да влизат през предната врата и да излизат от задната. Освен това нашите автобуси имат две групи стълби, свързващи двете нива: предната трябва да се използва за качване, а задната за слизане, за да спестим време и да направим пътуванията ни още по-приятни.\nБезплатен Wi-Fi на борда.Нашите автобуси разполагат с безплатен Wi-Fi, така че можете да сърфирате и да сте информирани, докато пътувате с нас.\nПлъзгащ се покривВ случай на дъжд, нашият персонал ще покрие горната палуба, за да можете да продължите да се наслаждавате на маршрута, дори когато времето стане лошо."],
#                 'Рецинте Модерниста': ["Pictures/Recinte.png", "Recinto Modernista de Sant Pau, разположен в Барселона, Испания, е архитектурен шедьовър, който стои като свидетелство за движението Modernisme. Проектиран от известния архитект Lluís Domènech i Montaner, този необикновен комплекс първоначално е бил построен като болница и е служил като фар за иновации и изцеление. Неговата зашеметяваща архитектура, украсена със сложни детайли и живи мозайки, демонстрира същността на каталунския модернистичен стил. Днес Recinto Modernista de Sant Pau е обект на световното наследство на ЮНЕСКО и е превърнат в културен център, приветстващ посетителите да изследват неговата богата история, забележителна архитектура и вдъхновяващи градини."]
#                 }
#
# allnavigations = {'към Аквариумът': ["Pictures/ToAquarium.png", "За да достигнете до Аквариума, можете да вървите около 35 минути от хотела по показания маршрут или да хванете автобус V17 и да стигнете за 20 минути.", "Акулите хапят! Но не през стъклото :)..\n","Pictures/ToAquariumBus.png"],
#                   'към Ел Понт Моста': ["Pictures/ToElPont.png", "За да достигнете до Мостът на Епископа, вървете около 20 минути от Аквариума по показания маршрут.","Не гледайте черепа на него прекалено дълго!Местните казват че е прокълнат.\n",None],
#                   'към Катедралата': ["Pictures/ToCathedral.png", "За да достигнете до Катедралата, вървете около 3 минути от Мостът на Епископа по показания маршрут.", "Не забравяйте да се качите и отгоре. Приятно разглеждане!\n",None],
#                   'към Пазарът': ["Pictures/ToMercado.png", "За да достигнете до пазарът, вървете около 10 минути от Катедралата по показания маршрут.", "Приятно пазарене и пазаруване!\n",None ],
#                   'към Ла Рамбла и Площада': ["Pictures/ToRambla.png", "За да достигнете до Ла Рамбла, вървете около 6 минути от пазарът по показания маршрут.", "Ла рамбла е известен с джебджийство!!!Пазете си джобовете и приятно разглеждане!\n",None],
#                   'към Палатът на музиката': ["Pictures/ToPalace.png", "За да достигнете до Палатът на музиката, вървете около 10 минути от Ла рамбла по показания маршрут.","Изпейте една песен ако имате смелост.Приятно разглеждане!\n",None],
#                   'към Саграда': ["Pictures/ToSagrada.png", "За да достигнете до Саграда, можете да вървите около 30 минути от хотела или да хванете Метро L2 и да стигнете за 12 минути.", "Приятно разглеждане на най-удивителната творба на Гауди!\n","Pictures/ToSagradaBus.png"],
#                   'към Гуел': ["Pictures/ToGuel.png", "За да достигнете до Гуел, можете да вървите около 40 минути от Саграда или да хванете Метро L5 и да стигнете за 20 минути и после да вървите още 10 минути през парка до централните му части.", "Приятно разглеждане на още творби на Гауди!\n","Pictures/ToGuelBus.png" ],
#                   'Към Мол Арена': ["Pictures/ToArenasBus.png", "За да достигнете до Мол Арена, ще са ви нужни 40 минути от Гуел.Вървете 10 минути през парка и хванете Метро L3 за 30 минути.", "Бикове вече там няма, можете да носите червено :)!\n",None],
#                   'към Лабиринта на Хорта': ["Pictures/ToLabyrinthBus.png", "За да достигнете до Лабиринта, ще са ви нужни 30 минути от Хотела.Хванете Метро L3 и да стигнете за 20 минути и после вървете още 10 минути през парка до централните му части.", "Не се губете вътре!\n",None],
#                   'към Къщите': ["Pictures/ToCasasBus.png", "За да достигнете до Къщите, вървете около 10 минути от парк лабиринта и хванете Метро L3,ще стигнете за 20 минути.Къщите се намират на 10 минути пеша една от друга.", "Приятно разглеждане на още творби на Гауди!\n",None],
#                   'към Монтжуик': ["Pictures/ToMontjuicBus.png", "За да достигнете до Монтжуик, ще ви отнеме около 50 минути от Къщите.Хванете Метро L3 и се прикачете на автобус 150 показан в маршрута.", "На връщане можете да се възползвате от кабинковия лифт за да се насладите на гледка на Барселона!\n",None],
#                   }
# restaurant_data = [
#         {"name": "Maná 75", "image": "Pictures/Mana.png", "info": "Maná 75 Разположен в квартал La Barceloneta, има толкова много характеристики, които да подчертаете за Maná 75, че е трудно да изберете само една. Сред първите неща, които привличат най-голямо внимание, е уютният му интериор. Когато влезете в Maná 75, усещате същността на най-топлата, най-утешителна и най-жизнена Барселона. Вътрешността на сградата е с много модерен, светъл и уникален вид.\n\nКухня: средиземноморска, здравословна, паеля, селекция от вина и кава.\nСредна цена: Между 35 и 45 евро на човек\nAddress: Passeig de Joan de Borbó, 101, Barcelona\nContact:+34 938 32 64 15"},
#         {"name": "RESTAURANT 7 PORTES", "image": "Pictures/7portes.png", "info": "Като ориентир в ресторантите в Барселона, той ви предлага обширно пътешествие през традиционната каталунска кухня, без да се отказвате от плахи международни кулинарни приноси. Класическата му декорация му придава много деликатна и уютна атмосфера, в която можете да изследвате, хапка по хапка, 185-годишната история, която този ресторант носи зад себе си.\n\nКухня: морска, средиземноморска, европейска, испанска, каталунска, международна\nСредна цена: Между 35 и 45 евро на човек\nAddress: Pg. d'Isabel II, 14, Ciutat Vella, 08003 Barcelona, Испания\nContact:+34 933 19 30 33"},
#         {"name": "VINITUS", "image": "Pictures/vinitus.png", "info": "Ако сте в Барселона, вероятно сте гладни за добри тапас. Не търсете повече, защото Cervecera Catalana ще ви даде всичко, което искате. Това място се управлява от същите хора, които управляват ресторант Vinitus, и това се вижда от храната и представянето. Този ресторант е известен с това, че дава добра стойност за това, което плащате, има бързо обслужване и притежава меню с много различни опции.\n\nКухня: средиземноморска, каталунска, тапас\nСредна цена: Между 20 и 30 евро на човек\nAddress: C. del Consell de Cent, 333 / C. Aragó, 282\nContact:+34 933 63 21 27"},
#         {"name": "CAN CORTADA", "image": "Pictures/cancortada.png", "info": "Кан Кортада е автентичен замък и част от художественото наследство на Барселона. От 1994 г., годината, в която отвори врати, този емблематичен ресторант предлага качествена каталунска кухня, специализирана в най-добрите меса.\n\nКухни: стек хаус, средиземноморска, испанска, каталунска\nСредна цена: Между 22 и 45 евро на човек\nAddress: Av. de l’Estatut de Catalunya, s/n\nContact:+34 934 27 23 15"},
#         {"name": "EL CHIGRE 1769", "image": "Pictures/chigre.png", "info": "El Chigre 1769 е каталонско-астурийски вермут и сайдер къща близо до парка Ciutadella. Работи с местни фермери и използва само органични продукти. Целта му е да зарадва вкусовите рецептори на всеки, който се осмели да опита сливането на каталунската и астурийската кухня.\n\nКухня: Средиземно море, синтез между Каталуния и Астурия.\nСредна цена: Между 15 и 40 евро на човек\nAddress: Carrer dels Sombrerers, 7\nContact:+34 937 82 63 30"},
#         {"name": "GALA RESTAURANTE BARCELONA", "image": "Pictures/gala.png", "info": "Новият модерен ресторант в Барселона и с добра причина. Открито сравнително наскоро, това емблематично място включва много неща наведнъж: въртележка, скрита зала за танци, четец на карти Таро, фонтан с форма на нос и трапезария (която също може да бъде малък театър , което прави това страхотно изживяване за хранене).\n\nКухня: Италиански, френски, международни, средиземноморски, испански, вегетариански варианти, вегански варианти\nСредна цена: Между 6 и 27 евро на човек\nAddress: C/ de Provença, 286\nContact:+34 936 07 37 70"},
#     ]
#
# clubs_data = [
#             {"name": "Pacha Barcelona", "image": "Pictures/pacha.png",
#              "info": "Световноизвестната марка Pacha носи невероятна музика и автентична атмосфера от Ибиса до Порт Олимпик в Барселона. Този клуб е перлата сред нощните клубове на пристанището и е отворен седем дни в седмицата! Клубове в стил Ибиса в най-чиста форма. Посетителите са посрещнати от елегантен бял интериор и зашеметяваща гледка към плажа. Разположен близо до плажа Барселонета, клубът привлича международна тълпа както с интелигентни, така и с непринудени емоции.\n\nМузика: Pacha Barcelona използва своята световна известност на марката, за да привлече в града най-добрите национални и международни диджеи на съвременната музикална сцена. За да ви даде представа, клубът наскоро посрещна артисти като Paco Osuna, Loco Dice и Dom Dolla.\nAddress:C/ de Ramon Trias Fargas, 2, Ciutat Vella\nContact:+34 647 83 57 51"},
#             {"name": "INPUT High Fidelity Dance Club", "image": "Pictures/input.png",
#              "info": "INPUT е в топ 3 на най-добрите места в града за слушане на електронна музика. Неговата гигантска звукова система Funktion One е достойна за всеки фестивал от първо ниво, а също и големият му LED екран не оставя никого безразличен. INPUT обикновено се посещава от рейвъри, които искат да танцуват и да развихрят въображението си. От младежи на двадесет години до хора на тридесет години, всички в INPUT са водени от една единствена страст: слушане на електронна музика по най-добрия възможен начин.\n\nAddress: Pg. d'Isabel II, 14, Ciutat Vella, 08003 Barcelona, Испания\nContact:+34 933 19 30 33"},
#             {"name": "Sala Apolo ", "image": "Pictures/apolo.png",
#              "info": "Това е един от нощните клубове с повече история и по-добър състав в Барселона. Повече от 75 години опит са доказателство за това. Apolo диша авангардизъм. Хората работят върху външния си вид, за да се отдалечат от ежедневието и да разрушат модните бариери. Бъди себе си. Обличайте се както се чувствате. Комфортът и танците са приоритет!\n\nМузика: Всяко парти има свой собствен музикален стил. Понеделник включва Honey Bunny и Bass Bunny с поп и международни хитове. В сряда известният Bresh! посещава Барселона заедно с градските звуци на Caníbal. В четвъртък Milkshake предлага многоцветна и ретро сесия, за да подгрее тълпата за грандиозното пристигане на Nitsa.\nAddress: C/ Nou de la Rambla, 113, Sants-Montjuïc, 08004\nContact:++34 934 41 40 01"},
#             {"name": "Dragon Weed Club", "image": "Pictures/dragon.png",
#              "info": "В Барселона Dragon Weed Club се превърна в икона. Повече от просто канабис клуб, това е топло и приветливо пространство, идеално за почивка и споделяне на хубави моменти.\n\nAddress: C/ del Bruc, 58, L'Eixample, 08009 Barcelona, Испания\nContact:+34931005276"},
#             {"name": "High Class Club", "image": "Pictures/high.png",
#              "info": "Този социален клуб за канабис излъчва елегантност и блясък от всеки ъгъл. Разполага с уникално и оригинално пространство, където всяко кътче е изпипано до най-малкия детайл.\n\nAddress: C. de Pujades, 147, Sant Martí, 08005 Barcelona, Испания"},
#             {"name": "Blue Dream Weed Club", "image": "Pictures/dream.png",
#              "info": "Blue Dream Weed се откроява като един от най-добрите клубове за канабис в Барселона, стратегически разположен в сърцето на града, в оживения квартал Sant Antoni. Този канабис клуб е истинско място за срещи за тези фенове на културата на канабис, които търсят комфортна, просторна и спокойна атмосфера, за да споделят своето хоби и да се срещат с нови хора.\n\nAddress: Carrer del Comte d'Urgell, 15, L'Eixample, 08011\nContact:+34 607 59 71 80"},
#         ]


# cursor.execute('''
#     CREATE TABLE alllocations (
#         name TEXT,
#         image_path TEXT,
#         description TEXT
#     )
# ''')

# cursor.execute('''
#     CREATE TABLE allnavigations (
#         destination TEXT,
#         onfoot_path TEXT,
#         description TEXT,
#         terminal_msg TEXT,
#         bus_image_path TEXT
#     )
# ''')
#
# cursor.execute('''
#     CREATE TABLE restaurants (
#         name TEXT,
#         image_path TEXT,
#         info TEXT
#     )
# ''')
#
# cursor.execute('''
#     CREATE TABLE clubs (
#         name TEXT,
#         image_path TEXT,
#         info TEXT
#     )
# ''')
#

# cursor.execute("drop table users")

# cursor.execute('''
#     CREATE TABLE users (
#         username TEXT,
#         hashed_password TEXT,
#         email TEXT,
#         birthdate TEXT,
#         years TEXT,
#         img_path TEXT
#     )
# ''')
#
# conn.commit()

#
# for name, data in alllocations.items():
#     image_path, description = data
#     cursor.execute("INSERT INTO alllocations (name, image_path, description) VALUES (?, ?, ?)",
#                    (name, image_path, description))
#
# for name, data in allnavigations.items():
#     if not data[3]:
#         onfoot_path, description, terminalmsg, publictransport_path = data
#         cursor.execute("INSERT INTO allnavigations (destination, onfoot_path, description, terminal_msg) VALUES (?, ?, ?, ?)",
#                          (name, onfoot_path, description, terminalmsg))
#     elif data[3]:
#         onfoot_path, description, terminalmsg, publictransport_path = data
#         cursor.execute(
#             "INSERT INTO allnavigations (destination, onfoot_path, description, terminal_msg, bus_image_path) VALUES (?, ?, ?, ?, ?)",
#             (name, onfoot_path, description, terminalmsg, publictransport_path))

# cursor.execute("DELETE FROM clubs")

# for item in clubs_data:
#  list=[]
#  for name,data in item.items():
#     list.append(data)
#  name, image_path, description = list
#  cursor.execute("INSERT INTO clubs (name, image_path, info) VALUES (?, ?, ?)",
#                    (name, image_path, description))

