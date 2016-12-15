class DayAttendance < ActiveRecord::Base
  belongs_to :subject_attendances
  has_many :student_statuses
end
