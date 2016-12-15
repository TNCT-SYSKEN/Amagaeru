class DayAttendance < ActiveRecord::Base
  belongs_to :subject_attendance
  has_many :student_statuses
end
