from src.model.User import User

def test_Validate_User_Data_is_complete():
  user = User(
    name="Nathiele",
    age=26,
    email="teste@teste.com"
  )
  created = user.validate_user()
  assert created == True


def test_Validate_User_Data_is_not_completes():
  user = User(
    name="Nathiele",
    age="",
    email="teste@teste.com"
  )
  created = user.validate_user()
  assert created == False
