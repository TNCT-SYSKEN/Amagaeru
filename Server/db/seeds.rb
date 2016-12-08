a = ["C", "E", "S", "M"]
4.times do |n|
  40.times do |m|
    first_name  = Faker::Name.first_name
    last_name = Faker::Name.last_name
    Student.create(depertment: a[n],
                   grade: n,
                   number: m + 1,
                   first_name: first_name,
                   last_name: last_name)
  end
end

Timetable.create(depertment: "C",
                 grade: 1)

d = ["Mon", "Tue", "Wed", "Thu", "Fri"]
5.times do |n|
  DayTimetable.create(timetable_id: 1,
                      day: d[n])
end

s = ["Japanese", "English", "Linear Algebra", "Political and Economy", "Physics", "Biology", "English Communication", "Computer Science", "World Histroy", "Chemistory"]
5.times do |n|
  Subject.create(name: s[n * 2],
                 start_time: "8:50",
                 finish_time: "10:20",
                 day_timetable_id: n + 1)

  Subject.create(name: s[n * 2 + 1],
                   start_time: "10:30",
                   finish_time: "12:00",
                   day_timetable_id: n + 1)
end
