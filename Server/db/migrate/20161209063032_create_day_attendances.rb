class CreateDayAttendances < ActiveRecord::Migration
  def change
    create_table :day_attendances do |t|
      t.integer :attendance_id
      t.integer :subject_attendance_id
      t.date :date

      t.timestamps null: false
    end
  end
end
