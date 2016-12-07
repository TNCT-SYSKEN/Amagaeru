class CreateSubjects < ActiveRecord::Migration
  def change
    create_table :subjects do |t|
      t.string :name
      t.time :start_time
      t.time :finish_time
      t.integer :day_timetable_id

      t.timestamps null: false
    end
  end
end
