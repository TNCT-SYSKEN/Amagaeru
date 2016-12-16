class CreateTimetables < ActiveRecord::Migration
  def change
    create_table :timetables do |t|
      t.string :depertment
      t.integer :grade

      t.timestamps null: false
    end
  end
end
