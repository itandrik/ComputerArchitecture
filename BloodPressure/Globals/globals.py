#menu string
menu_str = ("1. Show persons;",
            "2. Show doctors;",
            "3. Show diary;",
            "4. Add new person;",
            "5. Add new doctor;",
            "6. Add new record to diary;",
            "7. Delete person;"
            "8. Delete doctor;",
            "9. Delete record from diary;",
            "10. Change person characteristics;",
            "11. Change doctor characteristics;",
            "12. Change record in the diary;"
            "13. Change database")

error_message = "Wrong input!"
person_id_msg = "Enter person id : "
doctor_id_msg = "Enter doctor id : "

#SQL queries for work_with_db
select_sql = {
        "pressure_data":"SELECT (date,time,upper_level,"
        " lower_level, pulse, doctor_id_doctor)"
        " FROM pressure_data WHERE person_id_person=",
        "person":"SELECT * FROM person",
        "doctor":"SELECT * FROM doctor"
}
insert_sql = {
        "pressure_data":"(date,time,upper_level,"
        " lower_level, pulse, person_id_person, doctor_id_doctor)",
        "person":"(first_name,last_name,middle_name,age,weight,height,phone_number)",
        "doctor":"(first_name,last_name,middle_name,profession,phone_number)"
}
delete_sql = {
        "pressure_data":"id_pressure_data",
        "person":"id_person",
        "doctor":"id_doctor"
}

update_sql = {
        "pressure_data":["date=","time=","upper_level=",
                         "lower_level=","pulse=","person_id_person=",
                         "doctor_id_doctor="],
        "person":["first_name=", "last_name=", "middle_name=",
                  "age=", "weight=", "height=", "phone_number="],
        "doctor":["first_name=", "last_name=", "middle_name=",
                  "profession=", "phone_number="]
}

#Controller data
table_data = {
    "pressure_data": ("date", "time", "upper level", "lower level", "pulse", "person_id_person", "doctor_id_doctor"),
    "person": ("first name", "last name", "middle name", "age", "weight", "height", "phone_number"),
    "doctor": ("first name", "last name", "middle name", "profession", "phone number")
}
operations = {
    0: "load",
    1: "add",
    2: "delete",
    3: "change",
    4: "config"
}
tables = {
    0: "person",
    1: "doctor",
    2: "pressure_data"
}
databases = ("mysql", "sqlite", "postgreSQL")
