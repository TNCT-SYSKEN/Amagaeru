class Attendance < ActiveRecord::Base
  has_many :subject_attendances
end
