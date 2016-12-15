class SessionsController < ApplicationController
  def new
  end
  def create
    user = User.find_by(name: params[:session][:name].downcase)
    if user && user.authenticate(params[:session][:password])
      # ユーザーログイン後にユーザー情報のページにリダイレクトする
    else
      # エラーメッセージを作成する
      render 'new'
    end
  end

  def destroy
  end
end
