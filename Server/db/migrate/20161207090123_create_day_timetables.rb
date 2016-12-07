class CreateDayTimetables < ActiveRecord::Migration
  def change
    create_table :day_timetables do |t|

      t.timestamps null: false
    end
  end
end
