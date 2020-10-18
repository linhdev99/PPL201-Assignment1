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


    # Visit a parse tree produced by BKITParser#var_normal.
    def visitVar_normal(self, ctx:BKITParser.Var_normalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_vt.
    def visitVar_vt(self, ctx:BKITParser.Var_vtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_vp.
    def visitVar_vp(self, ctx:BKITParser.Var_vpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_vp.
    def visitArray_vp(self, ctx:BKITParser.Array_vpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body_declare.
    def visitBody_declare(self, ctx:BKITParser.Body_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declare.
    def visitFunc_declare(self, ctx:BKITParser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter_func.
    def visitParameter_func(self, ctx:BKITParser.Parameter_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elseif_stmt.
    def visitElseif_stmt(self, ctx:BKITParser.Elseif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_stmt.
    def visitElse_stmt(self, ctx:BKITParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#scalar_var.
    def visitScalar_var(self, ctx:BKITParser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_var.
    def visitIndex_var(self, ctx:BKITParser.Index_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#conditionExpr.
    def visitConditionExpr(self, ctx:BKITParser.ConditionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#updateExpr.
    def visitUpdateExpr(self, ctx:BKITParser.UpdateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#doWhile_stmt.
    def visitDoWhile_stmt(self, ctx:BKITParser.DoWhile_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_call.
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#op_index.
    def visitOp_index(self, ctx:BKITParser.Op_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operands_int.
    def visitOperands_int(self, ctx:BKITParser.Operands_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#all_lit.
    def visitAll_lit(self, ctx:BKITParser.All_litContext):
        return self.visitChildren(ctx)



del BKITParser