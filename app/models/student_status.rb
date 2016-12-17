class StudentStatus < ActiveRecord::Base
  belongs_to :day_attendance
  belongs_to :student
end
