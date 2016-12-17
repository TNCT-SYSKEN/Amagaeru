class CreateDayTimetables < ActiveRecord::Migration
  def change
    create_table :day_timetables do |t|
      t.integer :timetable_id
      t.string :day

      t.timestamps null: false
    end
  end
end
