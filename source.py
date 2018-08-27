    def add_cog(self, cog):

        """Adds a "cog" to the bot.



        A cog is a class that has its own event listeners and commands.



        They are meant as a way to organize multiple relevant commands

        into a singular class that shares some state or no state at all.



        The cog can also have a ``__global_check`` member function that allows

        you to define a global check. See :meth:`.check` for more info. If

        the name is ``__global_check_once`` then it's equivalent to the

        :meth:`.check_once` decorator.



        More information will be documented soon.



        Parameters

        -----------

        cog

            The cog to register to the bot.

        """



        self.cogs[type(cog).__name__] = cog



        try:

            check = getattr(cog, '_{.__class__.__name__}__global_check'.format(cog))

        except AttributeError:

            pass

        else:

            self.add_check(check)



        try:

            check = getattr(cog, '_{.__class__.__name__}__global_check_once'.format(cog))

        except AttributeError:

            pass

        else:

            self.add_check(check, call_once=True)



        members = inspect.getmembers(cog)

        for name, member in members:

            # register commands the cog has

            if isinstance(member, Command):

                if member.parent is None:

                    self.add_command(member)

                continue



            # register event listeners the cog has

            if name.startswith('on_'):

                self.add_listener(member, name)
