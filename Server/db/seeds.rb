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

Attendance.create(depertment: "C",
                  grade: 1)

10.times do |n|
  SubjectAttendance.create(subject_id: n + 1,
                           attendance_id: 1)
end

10.times do |n|
  r = rand(5)
  5.times do |m|
    DayAttendance.create(subject_attendance_id: n + 1,
                         date: "2016/04/" + (m * 7 + r).to_s)
  end
end

10.times do |l|
  5.times do |n|
    40.times do |m|
      StudentStatus.create(status: rand(2),
                           day_attendance_id: (5 * (l - 1)) + n,
                           student_id: m + 1)
    end
  end
end
