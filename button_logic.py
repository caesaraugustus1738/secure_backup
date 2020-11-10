from encryption import fernet_key_gen

    def _button_commands(self, buttons, skin):
        buttons['encrypt']['box'].config(command=lambda: self._key_gen(skin=skin, buttons=buttons))
        buttons['reset'].config(command=lambda: self._reset_inputs(skin=skin, buttons=buttons))
        buttons['archive'].config(command=lambda: self._archive(skin))


    def _get_inputs(self, skin):
        '''Get values from input fields.'''
        inputs = {
        'arc_path': skin['arc_path']['entry'].get(),
        'arc_dest': skin['arc_dest']['entry'].get(),
        'key': skin['key']['entry'].get()
        }
        return inputs


    def _archive(self, skin):
        self.backend.archive(self._get_inputs(skin))


    def _reset_inputs(self, skin, buttons):
        skin['arc_path']['var'].set(self._default_arc_path)
        skin['arc_dest']['var'].set(self._default_arc_dest)
        buttons['encrypt']['var'].set(0)
        self._key_gen(skin, buttons)


    def _key_gen(self, skin, buttons):
        if not buttons['encrypt']['var'].get():
            skin['key']['var'].set(self._default_key)
        else:
            key = fernet_key_gen()
            skin['key']['var'].set(key)