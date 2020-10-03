# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#main.
    def visitMain(self, ctx:BKITParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declare.
    def visitVar_declare(self, ctx:BKITParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_normal.
    def visitVar_normal(self, ctx:BKITParser.Var_normalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_array.
    def visitVar_array(self, ctx:BKITParser.Var_arrayContext):
        return self.visitChildren(ctx)



del BKITParser