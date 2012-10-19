
        # Integration tests for ClarifyIt
        ztc.ZopeDocFileSuite(
            'ClarifyIt.txt',
            package='collective.clarifyit',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),

