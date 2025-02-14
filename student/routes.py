

from controllers import student_controller

def register_routes(app):
    # 🟢 Authentication Routes
    app.add_url_rule('/register', 'register', student_controller.register, methods=['GET', 'POST'])
    app.add_url_rule('/login', 'login', student_controller.login, methods=['GET', 'POST'])
    app.add_url_rule('/logout', 'logout', student_controller.logout)

    # 🟢 Student Profile Routes
    app.add_url_rule('/profile', 'profile', student_controller.show_profile)
    app.add_url_rule('/profile/edit', 'edit_profile', student_controller.edit, methods=['GET', 'POST'])
    app.add_url_rule('/profile/delete', 'delete_profile', student_controller.delete, methods=['POST'])


