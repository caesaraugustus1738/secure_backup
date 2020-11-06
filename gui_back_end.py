import gui_front_end as frontend
import archive as a
import os

class Archiver:
    '''Perform logic on data received from front end.'''
    def __init__(self):
        self.gui = frontend.ArchiverGUI(self)
        self._default_key = self.gui._default_key


    def archive(self, inputs):
        v_inputs = inputs
        self.input_validation(v_inputs)
        print(v_inputs)
        archive = a.Archive(
            source=v_inputs['arc_path'], 
            dest=v_inputs['arc_dest'], 
            format_='zip'
        )
        archive.publish(key=v_inputs['key'], toc=True)
        print('Archive complete.')


    def unarchive(self):
        pass


    def input_validation(self, inputs):
        '''Data validation on inputs.'''
        val_inputs = inputs
        for k in inputs:
            print(f'Checking {val_inputs[k]}')
            if k == 'key':
                if val_inputs[k].strip() == self._default_key:
                    print('Archive will not be encrypted.')
                    val_inputs[k] = None
            else:
                if os.path.isdir(inputs[k]):
                    print('Input validated.')
                else:
                    raise Exception ('You must enter a valid path.')
        
        return val_inputs
            


# Generate a key and write it to a text file
                # key = fernet.Fernet.generate_key()
                # with open('key.txt', 'wb') as f:
                #   f.write(key)

                # # Read key
                # with open('key.txt', 'rb') as f:
                #   key = f.read()

                # # Create message
                # with open('message.txt', 'w') as f:
                #   f.write('My name is George Augustus Tully.')

                # # Read message into memory
                # with open('message.txt') as f:
                #   msg = f.read()

                # # Convert msg to bytes
                # b_msg = msg.encode()

                # # Plug symmetric private key into Fernet function
                # f_key = fernet.Fernet(key)

                # # Use method of Fernet object to encrypt message
                # encrypted_msg = f_key.encrypt(b_msg)

                # # Decrypt message
                # decrypted_msg = f_key.decrypt(encrypted_msg)


                # print(encrypted_msg, '\n', decrypted_msg)
                # print(decrypted_msg == encrypted_msg)
