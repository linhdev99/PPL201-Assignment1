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


    # Visit a parse tree produced by BKITParser#var_declare_stmt.
    def visitVar_declare_stmt(self, ctx:BKITParser.Var_declare_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_single.
    def visitVar_single(self, ctx:BKITParser.Var_singleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_list.
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declare_normal.
    def visitVar_declare_normal(self, ctx:BKITParser.Var_declare_normalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_normal.
    def visitVar_normal(self, ctx:BKITParser.Var_normalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_vt.
    def visitVar_vt(self, ctx:BKITParser.Var_vtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_vp.
    def visitVar_vp(self, ctx:BKITParser.Var_vpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_vp_int.
    def visitVar_vp_int(self, ctx:BKITParser.Var_vp_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_vp_float.
    def visitVar_vp_float(self, ctx:BKITParser.Var_vp_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_vp_string.
    def visitVar_vp_string(self, ctx:BKITParser.Var_vp_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_vt.
    def visitArray_vt(self, ctx:BKITParser.Array_vtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_vp.
    def visitArray_vp(self, ctx:BKITParser.Array_vpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#sb_value.
    def visitSb_value(self, ctx:BKITParser.Sb_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#cb_value.
    def visitCb_value(self, ctx:BKITParser.Cb_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declare.
    def visitFunc_declare(self, ctx:BKITParser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter_func.
    def visitParameter_func(self, ctx:BKITParser.Parameter_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_parameter.
    def visitVar_parameter(self, ctx:BKITParser.Var_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body_declare.
    def visitBody_declare(self, ctx:BKITParser.Body_declareContext):
        return self.visitChildren(ctx)



del BKITParser