class_AW = {
        "Kamal Singh": "6367615068",
        "Kritika Pandey": "6268938510",
        "Aditi Stuti":"9508660033",
        "Mansi Singh":"8303934546",
        "Amisha Bansal":"9569990704",
        "Deepali Shrivastav":"8931001730",
        "Pallavi Singh":"6204326370",
        "Harsh Sehrawat":"8396016718",
        "Rahul Kanyal":"6397090527",
        "Khushpreet Kaur":"6280878685",
        "Mohit Dua":"9599766609",
        "Isha ":"8950687682",
        "Sparsh Bansal":"6393006650",
        "Rechi ":"9550673648",
        "Kapil Lamba":"6377054831",
        "Ujjawal":"6376747170",
        "Sai Krishna":"6281271608",
        "Mohd. Afaq":"7727892007",
        "Gaurav Yadav":"7895806221",
        "Sakshi Khatri":"8306708813",
        "Navdeep Singh":"8530876498",
        "Dheeraj Thakur":"8629051279",
        "Sinan":"8714170520",
        "Naga Sai Reddy":"89193003762",
        "Rahul Rajeshwar":"9074031840",
        "Aditya Bhadade":"9168546881",
        "Sonu Choudhary":"9358421276",
        "Shivam Yadav":"9386840524",
        "Vignesh Inapakolla":"9391588556",
        "Suhaib Naik":"9622084629",
        "Sohil Sharma":"9675336153",
        "Prateek Agarwal":"9772159844",
        "Ritik Roshan Kumar":"9801830465",
        "Yash Jain":"8576942222",
        "Rahul Gupta":"8427533412",
        "Divyendra Kutapalli":"8263043261",
        "Arshil":"6393274424",
        "Deepak Kumar":"7634088256",
        "Abhay":"7900569319",
        "Ashutosh Singh":"7988842174",
        "Yunesh Kumar":"8000969036",
        "Sudarshan Reddy":"8074747385",
        "Nani Hanumanthu":"8106808412",
        "Shivam Prakash":"8368319653",
        "Simar":"9877675724",
        "Shivansh Pal":"8368310200",
        "Saqib Dar":"7006489594",
        "Roshan Mandal":"7478177365",
        "Kartikey Mishra":"7985966256",
        "Kartik":"7981376828",
        "Mohit Choudhary":"8824958436",
        "Shahid Sarvar": "9319801328",
        "Shivam": "9508187092",
        "Mashuk Farhan": "9633848403",
        "Tarun Choudhary": "9805394341",
        "Saad":"8340115069",
        "Arshdeep Singh": "7888401683",
        "Abhishek":"9508504054",
        "Ashutosh Negi":"8894649843",
        "Amrutha Harshini":"7672090471",
        }




print("Type name to get phone number.")
print("Type exit to exit.")
a=input("name: ")
while True:
    if a !="exit":
        if a.title() not in class_AW:
            print("Enter valid name.")
            a = input("Name: ")
        else:
            print(class_AW.get(a.title()))
            a = input("Name: ")
    else:
        break