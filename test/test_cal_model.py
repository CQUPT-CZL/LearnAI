#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agent测试模块
测试LearnAI项目中的agent是否正常工作
"""

import sys
import os
from unittest.mock import patch, MagicMock

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from langchain_core.messages import HumanMessage, AIMessage
from src.agent.my_agent import graph
from src.agent.utils.nodes import call_model, _get_model
from src.agent.utils.state import AgentState


class TestAgentModel:
    """测试Agent模型相关功能"""
    
    def test_get_model_with_env(self):
        """测试模型获取功能（需要环境变量）"""
        try:
            model = _get_model("deepseek")
            assert model is not None
            print("✅ 模型获取成功")
            return True
        except ValueError as e:
            if "API_KEY not found" in str(e):
                print("⚠️  请确保.env文件中配置了OPENAI_API_KEY")
                return False
            else:
                raise e
    
    def test_get_model_invalid_type(self):
        """测试无效模型类型"""
        try:
            _get_model("invalid_model")
            assert False, "应该抛出ValueError"
        except ValueError as e:
            if "Unsupported model type" in str(e):
                print("✅ 无效模型类型检测正常")
                return True
            else:
                raise e


class TestAgentNodes:
    """测试Agent节点功能"""
    
    @patch('src.agent.utils.nodes._get_model')
    def test_call_model_mock(self, mock_get_model):
        """使用Mock测试call_model函数"""
        # 创建Mock模型
        mock_model = MagicMock()
        mock_response = AIMessage(content="这是一个测试响应")
        mock_model.invoke.return_value = mock_response
        mock_get_model.return_value = mock_model
        
        # 测试状态
        test_state = {
            "messages": [HumanMessage(content="你好")]
        }
        
        # 调用函数
        result = call_model(test_state)
        
        # 验证结果
        assert "messages" in result
        assert len(result["messages"]) == 1
        assert result["messages"][0].content == "这是一个测试响应"
        print("✅ call_model函数测试通过")
        return True
    
    def test_call_model_real(self):
        """测试真实的call_model函数（需要API密钥）"""
        try:
            test_state = {
                "messages": [HumanMessage(content="请简单回答：1+1等于多少？")]
            }
            
            result = call_model(test_state)
            
            assert "messages" in result
            assert len(result["messages"]) == 1
            assert isinstance(result["messages"][0], AIMessage)
            print(f"✅ 真实API调用成功，响应: {result['messages'][0].content[:50]}...")
            return True
            
        except Exception as e:
            if "API_KEY not found" in str(e):
                print("⚠️  请确保.env文件中配置了OPENAI_API_KEY")
                return False
            else:
                print(f"❌ 真实API调用失败: {e}")
                raise e


class TestAgentGraph:
    """测试Agent图工作流"""
    
    @patch('src.agent.utils.nodes._get_model')
    def test_graph_invoke_mock(self, mock_get_model):
        """使用Mock测试图调用"""
        # 创建Mock模型
        mock_model = MagicMock()
        mock_response = AIMessage(content="Mock响应：你好！")
        mock_model.invoke.return_value = mock_response
        mock_get_model.return_value = mock_model
        
        # 测试输入
        initial_state = {
            "messages": [HumanMessage(content="你好")]
        }
        
        # 调用图
        result = graph.invoke(initial_state)
        
        # 验证结果
        assert "messages" in result
        assert len(result["messages"]) >= 2  # 原始消息 + AI响应
        assert isinstance(result["messages"][-1], AIMessage)
        print("✅ Agent图Mock测试通过")
        return True
    
    def test_graph_invoke_real(self):
        """测试真实的图调用（需要API密钥）"""
        try:
            initial_state = {
                "messages": [HumanMessage(content="请用一句话介绍你自己")]
            }
            
            result = graph.invoke(initial_state)
            
            assert "messages" in result
            assert len(result["messages"]) >= 2
            assert isinstance(result["messages"][-1], AIMessage)
            
            ai_response = result["messages"][-1].content
            print(f"✅ Agent图真实测试成功")
            print(f"AI响应: {ai_response}")
            return True
            
        except Exception as e:
            if "API_KEY not found" in str(e):
                print("⚠️  请确保.env文件中配置了OPENAI_API_KEY")
                return False
            else:
                print(f"❌ Agent图调用失败: {e}")
                raise e


class TestAgentIntegration:
    """集成测试"""
    
    def test_multiple_conversations(self):
        """测试多轮对话"""
        try:
            conversations = [
                "你好",
                "1+1等于多少？",
                "谢谢你的回答"
            ]
            
            messages = []
            
            for user_input in conversations:
                messages.append(HumanMessage(content=user_input))
                
                state = {"messages": messages.copy()}
                result = graph.invoke(state)
                
                # 添加AI响应到消息历史
                ai_response = result["messages"][-1]
                messages.append(ai_response)
                
                print(f"用户: {user_input}")
                print(f"AI: {ai_response.content[:100]}...")
                print("-" * 50)
            
            print("✅ 多轮对话测试成功")
            return True
            
        except Exception as e:
            if "API_KEY not found" in str(e):
                print("⚠️  请确保.env文件中配置了OPENAI_API_KEY")
                return False
            else:
                print(f"❌ 多轮对话测试失败: {e}")
                raise e


def run_manual_tests():
    """手动运行测试（不依赖pytest）"""
    print("=" * 60)
    print("LearnAI Agent 手动测试")
    print("=" * 60)
    
    # 测试模型获取
    print("\n1. 测试模型获取...")
    try:
        model = _get_model("deepseek")
        print("✅ 模型获取成功")
    except Exception as e:
        print(f"❌ 模型获取失败: {e}")
        if "API_KEY not found" in str(e):
            print("请确保在项目根目录创建.env文件，并添加以下内容:")
            print("OPENAI_API_KEY=your_api_key_here")
            print("OPENAI_API_BASE=your_api_base_url_here")
        return
    
    # 测试简单对话
    print("\n2. 测试简单对话...")
    try:
        initial_state = {
            "messages": [HumanMessage(content="你好，请简单介绍一下你自己")]
        }
        
        result = graph.invoke(initial_state)
        ai_response = result["messages"][-1].content
        
        print(f"用户: 你好，请简单介绍一下你自己")
        print(f"AI: {ai_response}")
        print("✅ 简单对话测试成功")
        
    except Exception as e:
        print(f"❌ 简单对话测试失败: {e}")
        return
    
    # 测试数学问题
    print("\n3. 测试数学问题...")
    try:
        initial_state = {
            "messages": [HumanMessage(content="请计算 15 + 27 = ?")]
        }
        
        result = graph.invoke(initial_state)
        ai_response = result["messages"][-1].content
        
        print(f"用户: 请计算 15 + 27 = ?")
        print(f"AI: {ai_response}")
        print("✅ 数学问题测试成功")
        
    except Exception as e:
        print(f"❌ 数学问题测试失败: {e}")
        return
    
    print("\n=" * 60)
    print("🎉 所有手动测试完成！")
    print("=" * 60)


def run_unit_tests():
    """运行单元测试"""
    print("=" * 60)
    print("LearnAI Agent 单元测试")
    print("=" * 60)
    
    test_results = []
    
    # 测试模型相关功能
    print("\n--- 测试模型功能 ---")
    model_tester = TestAgentModel()
    
    try:
        result = model_tester.test_get_model_with_env()
        test_results.append(("模型获取测试", result))
    except Exception as e:
        print(f"❌ 模型获取测试失败: {e}")
        test_results.append(("模型获取测试", False))
    
    try:
        result = model_tester.test_get_model_invalid_type()
        test_results.append(("无效模型类型测试", result))
    except Exception as e:
        print(f"❌ 无效模型类型测试失败: {e}")
        test_results.append(("无效模型类型测试", False))
    
    # 测试节点功能
    print("\n--- 测试节点功能 ---")
    node_tester = TestAgentNodes()
    
    try:
        result = node_tester.test_call_model_mock()
        test_results.append(("Mock模型调用测试", result))
    except Exception as e:
        print(f"❌ Mock模型调用测试失败: {e}")
        test_results.append(("Mock模型调用测试", False))
    
    try:
        result = node_tester.test_call_model_real()
        test_results.append(("真实模型调用测试", result))
    except Exception as e:
        print(f"❌ 真实模型调用测试失败: {e}")
        test_results.append(("真实模型调用测试", False))
    
    # 测试图功能
    print("\n--- 测试图工作流 ---")
    graph_tester = TestAgentGraph()
    
    try:
        result = graph_tester.test_graph_invoke_mock()
        test_results.append(("Mock图调用测试", result))
    except Exception as e:
        print(f"❌ Mock图调用测试失败: {e}")
        test_results.append(("Mock图调用测试", False))
    
    try:
        result = graph_tester.test_graph_invoke_real()
        test_results.append(("真实图调用测试", result))
    except Exception as e:
        print(f"❌ 真实图调用测试失败: {e}")
        test_results.append(("真实图调用测试", False))
    
    # 集成测试
    print("\n--- 集成测试 ---")
    integration_tester = TestAgentIntegration()
    
    try:
        result = integration_tester.test_multiple_conversations()
        test_results.append(("多轮对话测试", result))
    except Exception as e:
        print(f"❌ 多轮对话测试失败: {e}")
        test_results.append(("多轮对话测试", False))
    
    # 输出测试结果摘要
    print("\n" + "=" * 60)
    print("测试结果摘要")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for test_name, result in test_results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
        else:
            failed += 1
    
    print(f"\n总计: {passed + failed} 个测试")
    print(f"通过: {passed} 个")
    print(f"失败: {failed} 个")
    
    if failed == 0:
        print("\n🎉 所有测试都通过了！")
    else:
        print(f"\n⚠️  有 {failed} 个测试失败，请检查配置和代码")


if __name__ == "__main__":
    # 检查是否有命令行参数
    if len(sys.argv) > 1:
        if sys.argv[1] == "manual":
            run_manual_tests()
        elif sys.argv[1] == "unit":
            run_unit_tests()
        else:
            print(f"未知参数: {sys.argv[1]}")
    else:
        print("LearnAI Agent 测试工具")
        print("=" * 40)
        print("使用方法:")
        print("1. 运行手动测试: python test/test_cal_model.py manual")
        print("2. 运行单元测试: python test/test_cal_model.py unit")
        print("\n注意: 真实API测试需要在.env文件中配置API密钥")