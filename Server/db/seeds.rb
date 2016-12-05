99.times do |n|
  first_name  = Faker::Name.first_name
  last_name = Faker::Name.last_name
  Student.create(depertment: "C",
                 grade: 2,
                 number: n + 1,
                 first_name: first_name,
                 last_name: last_name)
end
