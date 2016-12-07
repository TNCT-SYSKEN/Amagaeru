class DayTimetable < ActiveRecord::Base
  belongs_to :timetable
  has_many :day_timetables
end
