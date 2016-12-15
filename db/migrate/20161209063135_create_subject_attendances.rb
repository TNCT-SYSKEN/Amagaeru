class CreateSubjectAttendances < ActiveRecord::Migration
  def change
    create_table :subject_attendances do |t|
      t.integer :subject_id
      t.integer :attendance_id

      t.timestamps null: false
    end
  end
end
