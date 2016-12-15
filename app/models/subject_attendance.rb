class SubjectAttendance < ActiveRecord::Base
  belongs_to :subject
  belongs_to :attendance
  has_many :day_attendances
end
