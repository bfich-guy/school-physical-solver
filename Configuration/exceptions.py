#region Custom exceptions

class ArrayIsNotDecimal(Exception):
    pass

#endregion


#region Error messages

error_messages_dict: dict[type[Exception], str] = {

    ArrayIsNotDecimal: "Неверный ввод. Просим вас вводить числа. Для написания дробных чисел используйте точку и при том только одну.",

}