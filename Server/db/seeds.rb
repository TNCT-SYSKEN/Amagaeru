a = ["C", "E", "S", "M"]
4.times do |n|
  40.times do |m|
    first_name  = Faker::Name.first_name
    last_name = Faker::Name.last_name
    Student.create(depertment: a[n],
                   grade: n + 1,
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

s = ["古文", "英語", "線形代数", "政治経済", "物理", "生物", "コミュニケーション英語", "情報工学", "世界史", "化学", "微分積分", "倫理", "英語表現", "情報リテラシー", "現代文", "地学", "コンピュータ概論", "プログラミング", "応用数学", "工学実験"]

5.times do |n|
  Subject.create(name: s[n * 4],
                 start_time: "8:50",
                 finish_time: "10:20",
                 day_timetable_id: n + 1)

  Subject.create(name: s[n * 4 + 1],
                   start_time: "10:30",
                   finish_time: "12:00",
                   day_timetable_id: n + 1)

  Subject.create(name: s[n * 4 + 2],
                 start_time: "12:50",
                 finish_time: "14:20",
                 day_timetable_id: n + 1)

  Subject.create(name: s[n * 4 + 3],
                 start_time: "14:40",
                 finish_time: "16:10",
                 day_timetable_id: n + 1)
end

Attendance.create(depertment: "C",
                  grade: 1)

Attendance.create(depertment: "E",
                  grade: 2)

Attendance.create(depertment: "S",
                  grade: 3)

Attendance.create(depertment: "M",
                  grade: 4)
4.times do |a|
  20.times do |n|
    SubjectAttendance.create(subject_id: n + 1,
                             attendance_id: a + 1)
    d = n / 4

    4.times do |m|
      DayAttendance.create(attendance_id: a + 1,
                           subject_attendance_id: (4 * a) + n + 1,
                           date: "2016-04-" + (Date.commercial(2016, 14 + m) + d).day.to_s)
      40.times do |l|
        StudentStatus.create(status: rand(2),
                             day_attendance_id: (80 * a + 4 * n) + m + 1,
                             student_id: l + 1)
      end
    end
  end
end
