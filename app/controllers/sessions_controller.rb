class SessionsController < ApplicationController
  def new
  end
  def create
    user = User.find_by_name params[:name]
    if user && user.authenticate(params[:session][:password])
      # ユーザーログイン後にユーザー情報のページにリダイレクトする
      log_in user
    if user.authority?
      redirect_to sessions_menu_path
      return
    else
      redirect_to attendances_index_path
    end
    else
      # エラーメッセージを作成する
      flash.now[:danger] = 'Invalid email/password combination'
      render 'new'
    end
  end
  def user_params
    params
  end
  def destroy
    log_out
    redirect_to "login"

  end
  def menu
  end
end
